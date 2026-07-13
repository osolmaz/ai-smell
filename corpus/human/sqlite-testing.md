# 1. Introduction

The reliability and robustness of SQLite is achieved in part by thorough and careful testing.

As of version 3.42.0(2023-05-16), the SQLite library consists of approximately 155.8 KSLOC of C code. (KSLOC means thousands of "Source Lines Of Code" or, in other words, lines of code excluding blank lines and comments.) By comparison, the project has 590 times as much test code and test scripts - 92053.1 KSLOC.

## 1.1. Executive Summary

- Four independently developed test harnesses
- 100% branch test coverage in an as-deployed configuration
- Millions and millions of test cases
- Out-of-memory tests
- I/O error tests
- Crash and power loss tests
- Fuzz tests
- Boundary value tests
- Disabled optimization tests
- Regression tests
- Malformed database tests
- Extensive use of assert() and run-time checks
- Valgrind analysis
- Undefined behavior checks
- Checklists

# 2. Test Harnesses

There are four independent test harnesses used for testing the core SQLite library. Each test harness is designed, maintained, and managed separately from the others.

The TCL Tests are the original tests for SQLite. They are contained in the same source tree as the SQLite core and like the SQLite core are in the public domain. The TCL tests are the primary tests used during development. The TCL tests are written using the TCL scripting language. The TCL test harness itself consists of 27.2 KSLOC of C code used to create the TCL interface. The test scripts are contained in 1390 files totaling 23.2MB in size. There are 51445 distinct test cases, but many of the test cases are parameterized and run multiple times (with different parameters) so that on a full test run millions of separate tests are performed.

The TH3 test harness is a set of proprietary tests, written in C that provide 100% branch test coverage (and 100% MC/DC test coverage) to the core SQLite library. The TH3 tests are designed to run on embedded and specialized platforms that would not easily support TCL or other workstation services. TH3 tests use only the published SQLite interfaces. TH3 consists of about 76.9 MB or 1055.4 KSLOC of C code implementing 50362 distinct test cases. TH3 tests are heavily parameterized, though, so a full-coverage test runs about 2.4 million different test instances. The cases that provide 100% branch test coverage constitute a subset of the total TH3 test suite. A soak test prior to release does about 248.5 million tests. Additional information on TH3 is available separately.

The SQL Logic Test or SLT test harness is used to run huge numbers of SQL statements against both SQLite and several other SQL database engines and verify that they all get the same answers. SLT currently compares SQLite against PostgreSQL, MySQL, Microsoft SQL Server, and Oracle 10g. SLT runs 7.2 million queries comprising 1.12GB of test data.

The dbsqlfuzz engine is a proprietary fuzz tester. Other fuzzers for SQLite mutate either the SQL inputs or the database file. Dbsqlfuzz mutates both the SQL and the database file at the same time, and is thus able to reach new error states. Dbsqlfuzz is built using the libFuzzer framework of LLVM with a custom mutator. There are 336 seed files. The dbsqlfuzz fuzzer runs about one billion test mutations per day. Dbsqlfuzz helps ensure that SQLite is robust against attack via malicious SQL or database inputs.

In addition to the four main test harnesses, there are many other small programs that implement specialized tests. Here are a few examples:

1. The "speedtest1.c" program estimates the performance of SQLite under a typical workload.
2. The "mptester.c" program is a stress test for multiple processes concurrently reading and writing a single database.
3. The "threadtest3.c" program is a stress test for multiple threads using SQLite simultaneously.
4. The "fuzzershell.c" program is used to run some fuzz tests.
5. The "jfuzz" program is a libfuzzer-based fuzzer for JSONB inputs to the JSON SQL functions.

All of the tests above must run successfully, on multiple platforms and under multiple compile-time configurations, before each release of SQLite.

Prior to each check-in to the SQLite source tree, developers typically run a subset (called "veryquick") of the Tcl tests consisting of about 304.7 thousand test cases. The veryquick tests include most tests other than the anomaly, fuzz, and soak tests. The idea behind the veryquick tests are that they are sufficient to catch most errors, but also run in only a few minutes instead of a few hours.

# 3. Anomaly Testing

Anomaly tests are tests designed to verify the correct behavior of SQLite when something goes wrong. It is (relatively) easy to build an SQL database engine that behaves correctly on well-formed inputs on a fully functional computer. It is more difficult to build a system that responds sanely to invalid inputs and continues to function following system malfunctions. The anomaly tests are designed to verify the latter behavior.

## 3.1. Out-Of-Memory Testing

SQLite, like all SQL database engines, makes extensive use of malloc() (See the separate report on dynamic memory allocation in SQLite for additional detail.) On servers and workstations, malloc() never fails in practice and so correct handling of out-of-memory (OOM) errors is not particularly important. But on embedded devices, OOM errors are frighteningly common and since SQLite is frequently used on embedded devices, it is important that SQLite be able to gracefully handle OOM errors.

OOM testing is accomplished by simulating OOM errors. SQLite allows an application to substitute an alternative malloc() implementation using the sqlite3_config(SQLITE_CONFIG_MALLOC,...) interface. The TCL and TH3 test harnesses are both capable of inserting a modified version of malloc() that can be rigged to fail after a certain number of allocations. These instrumented mallocs can be set to fail only once and then start working again, or to continue failing after the first failure. OOM tests are done in a loop. On the first iteration of the loop, the instrumented malloc is rigged to fail on the first allocation. Then some SQLite operation is carried out and checks are done to make sure SQLite handled the OOM error correctly. Then the time-to-failure counter on the instrumented malloc is increased by one and the test is repeated. The loop continues until the entire operation runs to completion without ever encountering a simulated OOM failure. Tests like this are run twice, once with the instrumented malloc set to fail only once, and again with the instrumented malloc set to fail continuously after the first failure.

## 3.2. I/O Error Testing

I/O error testing seeks to verify that SQLite responds sanely to failed I/O operations. I/O errors might result from a full disk drive, malfunctioning disk hardware, network outages when using a network file system, system configuration or permission changes that occur in the middle of an SQL operation, or other hardware or operating system malfunctions. Whatever the cause, it is important that SQLite be able to respond correctly to these errors and I/O error testing seeks to verify that it does.

I/O error testing is similar in concept to OOM testing; I/O errors are simulated and checks are made to verify that SQLite responds correctly to the simulated errors. I/O errors are simulated in both the TCL and TH3 test harnesses by inserting a new Virtual File System object that is specially rigged to simulate an I/O error after a set number of I/O operations. As with OOM error testing, the I/O error simulators can be set to fail just once, or to fail continuously after the first failure. Tests are run in a loop, slowly increasing the point of failure until the test case runs to completion without error. The loop is run twice, once with the I/O error simulator set to simulate only a single failure and a second time with it set to fail all I/O operations after the first failure.

In I/O error tests, after the I/O error simulation failure mechanism is disabled, the database is examined using PRAGMA integrity_check to make sure that the I/O error has not introduced database corruption.

## 3.3. Crash Testing

Crash testing seeks to demonstrate that an SQLite database will not go corrupt if the application or operating system crashes or if there is a power failure in the middle of a database update. A separate white-paper titled Atomic Commit in SQLite describes the defensive measures SQLite takes to prevent database corruption following a crash. Crash tests strive to verify that those defensive measures are working correctly.

It is impractical to do crash testing using real power failures, of course, and so crash testing is done in simulation. An alternative Virtual File System is inserted that allows the test harness to simulate the state of the database file following a crash.

In the TCL test harness, the crash simulation is done in a separate process. The main testing process spawns a child process which runs some SQLite operation and randomly crashes somewhere in the middle of a write operation. A special VFS randomly reorders and corrupts the unsynchronized write operations to simulate the effect of buffered filesystems. After the child dies, the original test process opens and reads the test database and verifies that the changes attempted by the child either completed successfully or else were completely rolled back. The integrity_check PRAGMA is used to make sure no database corruption occurs.

The TH3 test harness needs to run on embedded systems that do not necessarily have the ability to spawn child processes, so it uses an in-memory VFS to simulate crashes. The in-memory VFS can be rigged to make a snapshot of the entire filesystem after a set number of I/O operations. Crash tests run in a loop. On each iteration of the loop, the point at which a snapshot is made is advanced until the SQLite operations being tested run to completion without ever hitting a snapshot. Within the loop, after the SQLite operation under test has completed, the filesystem is reverted to the snapshot and random file damage is introduced that is characteristic of the kinds of damage one expects to see following a power loss. Then the database is opened and checks are made to ensure that it is well-formed and that the transaction either ran to completion or was completely rolled back. The interior of the loop is repeated multiple times for each snapshot with different random damage each time.

## 3.4. Compound failure tests

The test suites for SQLite also explore the result of stacking multiple failures. For example, tests are run to ensure correct behavior when an I/O error or OOM fault occurs while trying to recover from a prior crash.

# 4. Fuzz Testing

Fuzz testing seeks to establish that SQLite responds correctly to invalid, out-of-range, or malformed inputs.

## 4.1. SQL Fuzz

SQL fuzz testing consists of creating syntactically correct yet wildly nonsensical SQL statements and feeding them to SQLite to see what it will do with them. Usually some kind of error is returned (such as "no such table"). Sometimes, purely by chance, the SQL statement also happens to be semantically correct. In that case, the resulting prepared statement is run to make sure it gives a reasonable result.

### 4.1.1. SQL Fuzz Using The American Fuzzy Lop Fuzzer

The concept of fuzz testing has been around for decades, but fuzz testing was not an effective way to find bugs until 2014 when Michal Zalewski invented the first practical profile-guided fuzzer, American Fuzzy Lop or "AFL". Unlike prior fuzzers that blindly generate random inputs, AFL instruments the program being tested (by modifying the assembly-language output from the C compiler) and uses that instrumentation to detect when an input causes the program to do something different - to follow a new control path or loop a different number of times. Inputs that provoke new behavior are retained and further mutated. In this way, AFL is able to "discover" new behaviors of the program under test, including behaviors that were never envisioned by the designers.

AFL proved adept at finding arcane bugs in SQLite. Most of the findings have been assert() statements where the conditional was false under obscure circumstances. But AFL has also found a fair number of crash bugs in SQLite, and even a few cases where SQLite computed incorrect results.

Because of its past success, AFL became a standard part of the testing strategy for SQLite beginning with version 3.8.10(2015-05-07) until it was superseded by better fuzzers in version 3.29.0(2019-07-10).

### 4.1.2. Google OSS Fuzz

Beginning in 2016, a team of engineers at Google started the OSS Fuzz project. OSS Fuzz uses a AFL-style guided fuzzer running on Google's infrastructure. The Fuzzer automatically downloads the latest check-ins for participating projects, fuzzes them, and sends email to the developers reporting any problems. When a fix is checked in, the fuzzer automatically detects this and emails a confirmation to the developers.

SQLite is one of many open-source projects that OSS Fuzz tests. The test/ossfuzz.c source file in the SQLite repository is SQLite's interface to OSS fuzz.

OSS Fuzz no longer finds historical bugs in SQLite. But it is still running and does occasionally find issues in new development check-ins. Examples: [1] [2] [3].

### 4.1.3. The dbsqlfuzz and jfuzz fuzzers

Beginning in late 2018, SQLite has been fuzzed using a proprietary fuzzer called "dbsqlfuzz". Dbsqlfuzz is built using the libFuzzer framework of LLVM.

The dbsqlfuzz fuzzer mutates both the SQL input and the database file at the same time. Dbsqlfuzz uses a custom Structure-Aware Mutator on a specialized input file that defines both an input database and SQL text to be run against that database. Because it mutates both the input database and the input SQL at the same time, dbsqlfuzz has been able to find some obscure faults in SQLite that were missed by prior fuzzers that mutated only SQL inputs or only the database file. The SQLite developers keep dbsqlfuzz running against trunk in about 16 cores at all times. Each instance of dbsqlfuzz program is able to evalutes about 400 test cases per second, meaning that about 500 million cases are checked every day.

The dbsqlfuzz fuzzer has been very successful at hardening the SQLite code base against malicious attack. Since dbsqlfuzz has been added to the SQLite internal test suite, bug reports from external fuzzers such as OSSFuzz have all but stopped.

Note that dbsqlfuzz is not the Protobuf-based structure-aware fuzzer for SQLite that is used by Chromium and described in the Structure-Aware Mutator article. There is no connection between these two fuzzers, other than the fact that they are both based on libFuzzer The Protobuf fuzzer for SQLite is written and maintained by the Chromium team at Google, whereas dbsqlfuzz is written and maintained by the original SQLite developers. Having multiple independently-developed fuzzers for SQLite is good, as it means that obscure issues are more likely to be uncovered.

Near the end of January 2024, a second libFuzzer-based tool called "jfuzz" came into use. Jfuzz generates corrupt JSONB blobs and feeds them into the JSON SQL functions to verify that the JSON functions are able to safely and efficiently deal with corrupt binary inputs.

### 4.1.4. Other third-party fuzzers

SQLite seems to be a popular target for third-parties to fuzz. The developers hear about many attempts to fuzz SQLite and they do occasionally get bug reports found by independent fuzzers. All such reports are promptly fixed, so the product is improved and that the entire SQLite user community benefits. This mechanism of having many independent testers is similar to Linus's law: "given enough eyeballs, all bugs are shallow".

One fuzzing researcher of particular note is Manuel Rigger. Most fuzzers only look for assertion faults, crashes, undefined behavior (UB), or other easily detected anomalies. Dr. Rigger's fuzzers, on the other hand, are able to find cases where SQLite computes an incorrect answer. Rigger has found many such cases. Most of these finds are obscure corner cases involving type conversions and affinity transformations, and a good number of the finds are against unreleased features. Nevertheless, his finds are still important as they are real bugs, and the SQLite developers are grateful to be able to identify and fix the underlying problems.

### 4.1.5. The fuzzcheck test harness

Historical test cases from AFL, OSS Fuzz, and dbsqlfuzz are collected in a set of database files in the main SQLite source tree and then rerun by the "fuzzcheck" utility program whenever one runs "make test". Fuzzcheck only runs a few thousand "interesting" cases out of the billions of cases that the various fuzzers have examined over the years. "Interesting" cases are cases that exhibit previously unseen behavior. Actual bugs found by fuzzers are always included among the interesting test cases, but most of the cases run by fuzzcheck were never actual bugs.

### 4.1.6. Tension Between Fuzz Testing And 100% MC/DC Testing

Fuzz testing and 100% MC/DC testing are in tension with one another. That is to say, code tested to 100% MC/DC will tend to be more vulnerable to problems found by fuzzing and code that performs well during fuzz testing will tend to have (much) less than 100% MC/DC. This is because MC/DC testing discourages defensive code with unreachable branches, but without defensive code, a fuzzer is more likely to find a path that causes problems. MC/DC testing seems to work well for building code that is robust during normal use, whereas fuzz testing is good for building code that is robust against malicious attack.

Of course, users would prefer code that is both robust in normal use and resistant to malicious attack. The SQLite developers are dedicated to providing that. The purpose of this section is merely to point out that doing both at the same time is difficult.

For much of its history SQLite has been focused on 100% MC/DC testing. Resistance to fuzzing attacks only became a concern with the introduction of AFL in 2014. For a while there, fuzzers were finding many problems in SQLite. In more recent years, the testing strategy of SQLite has evolved to place more emphasis on fuzz testing. We still maintain 100% MC/DC of the core SQLite code, but most testing CPU cycles are now devoted to fuzzing.

While fuzz testing and 100% MC/DC testing are in tension, they are not completely at cross-purposes. The fact that the SQlite test suite does test to 100% MC/DC means that when fuzzers do find problems, those problems can be fixed quickly and with little risk of introducing new errors.

## 4.2. Malformed Database Files

There are numerous test cases that verify that SQLite is able to deal with malformed database files. These tests first build a well-formed database file, then add corruption by changing one or more bytes in the file by some means other than SQLite. Then SQLite is used to read the database. In some cases, the bytes changes are in the middle of data. This causes the content of the database to change while keeping the database well-formed. In other cases, unused bytes of the file are modified, which has no effect on the integrity of the database. The interesting cases are when bytes of the file that define database structure get changed. The malformed database tests verify that SQLite finds the file format errors and reports them using the SQLITE_CORRUPT return code without overflowing buffers, dereferencing NULL pointers, or performing other unwholesome actions.

The dbsqlfuzz fuzzer also does an excellent job of verifying that SQLite responds sanely to malformed database files.

## 4.3. Boundary Value Tests

SQLite defines certain limits on its operation, such as the maximum number of columns in a table, the maximum length of an SQL statement, or the maximum value of an integer. The TCL and TH3 test suites both contains numerous tests that push SQLite right to the edge of its defined limits and verify that it performs correctly for all allowed values. Additional tests go beyond the defined limits and verify that SQLite correctly returns errors. The source code contains testcase macros to verify that both sides of each boundary have been tested.

# 5. Regression Testing

Whenever a bug is reported against SQLite, that bug is not considered fixed until new test cases that would exhibit the bug have been added to either the TCL or TH3 test suites. Over the years, this has resulted in thousands and thousands of new tests. These regression tests ensure that bugs that have been fixed in the past are not reintroduced into future versions of SQLite.

# 6. Automatic Resource Leak Detection

Resource leak occurs when system resources are allocated and never freed. The most troublesome resource leaks in many applications are memory leaks - when memory is allocated using malloc() but never released using free(). But other kinds of resources can also be leaked: file descriptors, threads, mutexes, etc.

Both the TCL and TH3 test harnesses automatically track system resources and report resource leaks on every test run. No special configuration or setup is required. The test harnesses are especially vigilant with regard to memory leaks. If a change causes a memory leak, the test harnesses will recognize this quickly. SQLite is designed to never leak memory, even after an exception such as an OOM error or disk I/O error. The test harnesses are zealous to enforce this.

# 7. Test Coverage

The SQLite core, including the unix VFS, has 100% branch test coverage under TH3 in its default configuration as measured by gcov. Extensions such as FTS3 and RTree are excluded from this analysis.

## 7.1. Statement versus branch coverage

There are many ways to measure test coverage. The most popular metric is "statement coverage". When you hear someone say that their program as "XX% test coverage" without further explanation, they usually mean statement coverage. Statement coverage measures what percentage of lines of code are executed at least once by the test suite.

Branch coverage is more rigorous than statement coverage. Branch coverage measures the number of machine-code branch instructions that are evaluated at least once on both directions.

To illustrate the difference between statement coverage and branch coverage, consider the following hypothetical line of C code:

```
if( a>b && c!=25 ){ d++; }

```

Such a line of C code might generate a dozen separate machine code instructions. If any one of those instructions is ever evaluated, then we say that the statement has been tested. So, for example, it might be the case that the conditional expression is always false and the "d" variable is never incremented. Even so, statement coverage counts this line of code as having been tested.

Branch coverage is more strict. With branch coverage, each test and each subblock within the statement is considered separately. In order to achieve 100% branch coverage in the example above, there must be at least three test cases:

- a<=b
- a>b && c==25
- a>b && c!=25

Any one of the above test cases would provide 100% statement coverage but all three are required for 100% branch coverage. Generally speaking, 100% branch coverage implies 100% statement coverage, but the converse is not true. To reemphasize, the TH3 test harness for SQLite provides the stronger form of test coverage - 100% branch test coverage.

## 7.2. Coverage testing of defensive code

A well-written C program will typically contain some defensive conditionals which in practice are always true or always false. This leads to a programming dilemma: Does one remove defensive code in order to obtain 100% branch coverage?

In SQLite, the answer to the previous question is "no". For testing purposes, the SQLite source code defines macros called ALWAYS() and NEVER(). The ALWAYS() macro surrounds conditions which are expected to always evaluate as true and NEVER() surrounds conditions that are always evaluated to false. These macros serve as comments to indicate that the conditions are defensive code. In release builds, these macros are pass-throughs:

```
#define ALWAYS(X)  (X)
#define NEVER(X)   (X)

```

During most testing, however, these macros will throw an assertion fault if their argument does not have the expected truth value. This alerts the developers quickly to incorrect design assumptions.

```
#define ALWAYS(X)  ((X)?1:assert(0),0)
#define NEVER(X)   ((X)?assert(0),1:0)

```

When measuring test coverage, these macros are defined to be constant truth values so that they do not generate assembly language branch instructions, and hence do not come into play when calculating the branch coverage:

```
#define ALWAYS(X)  (1)
#define NEVER(X)   (0)

```

The test suite is designed to be run three times, once for each of the ALWAYS() and NEVER() definitions shown above. All three test runs should yield exactly the same result. There is a run-time test using the sqlite3_test_control(SQLITE_TESTCTRL_ALWAYS, ...) interface that can be used to verify that the macros are correctly set to the first form (the pass-through form) for deployment.

## 7.3. Forcing coverage of boundary values and boolean vector tests

Another macro used in conjunction with test coverage measurement is the testcase() macro. The argument is a condition for which we want test cases that evaluate to both true and false. In non-coverage builds (that is to say, in release builds) the testcase() macro is a no-op:

```
#define testcase(X)

```

But in a coverage measuring build, the testcase() macro generates code that evaluates the conditional expression in its argument. Then during analysis, a check is made to ensure tests exist that evaluate the conditional to both true and false. Testcase() macros are used, for example, to help verify that boundary values are tested. For example:

```
testcase( a==b );
testcase( a==b+1 );
if( a>b && c!=25 ){ d++; }

```

Testcase macros are also used when two or more cases of a switch statement go to the same block of code, to make sure that the code was reached for all cases:

```
switch( op ){
  case OP_Add:
  case OP_Subtract: {
    testcase( op==OP_Add );
    testcase( op==OP_Subtract );
    /* ... */
    break;
  }
  /* ... */
}

```

For bitmask tests, testcase() macros are used to verify that every bit of the bitmask affects the outcome. For example, in the following block of code, the condition is true if the mask contains either of two bits indicating either a MAIN_DB or a TEMP_DB is being opened. The testcase() macros that precede the if statement verify that both cases are tested:

```
testcase( mask & SQLITE_OPEN_MAIN_DB );
testcase( mask & SQLITE_OPEN_TEMP_DB );
if( (mask & (SQLITE_OPEN_MAIN_DB|SQLITE_OPEN_TEMP_DB))!=0 ){ ... }

```

The SQLite source code contains 1184 uses of the testcase() macro.

## 7.4. Branch coverage versus MC/DC

Two methods of measuring test coverage were described above: "statement" and "branch" coverage. There are many other test coverage metrics besides these two. Another popular metric is "Modified Condition/Decision Coverage" or MC/DC. Wikipedia defines MC/DC as follows:

- Each decision tries every possible outcome.
- Each condition in a decision takes on every possible outcome.
- Each entry and exit point is invoked.
- Each condition in a decision is shown to independently affect the outcome of the decision.

In the C programming language where && and || are "short-circuit" operators, MC/DC and branch coverage are very nearly the same thing. The primary difference is in boolean vector tests. One can test for any of several bits in bit-vector and still obtain 100% branch test coverage even though the second element of MC/DC - the requirement that each condition in a decision take on every possible outcome - might not be satisfied.

SQLite uses testcase() macros as described in the previous subsection to make sure that every condition in a bit-vector decision takes on every possible outcome. In this way, SQLite also achieves 100% MC/DC in addition to 100% branch coverage.

## 7.5. Measuring branch coverage

Branch coverage in SQLite is currently measured using gcov with the "-b" option. First the test program is compiled using options "-g -fprofile-arcs -ftest-coverage" and then the test program is run. Then "gcov -b" is run to generate a coverage report. The coverage report is verbose and inconvenient to read, so the gcov-generated report is processed using some simple scripts to put it into a more human-friendly format. This entire process is automated using scripts, of course.

Note that running SQLite with gcov is not a test of SQLite — it is a test of the test suite. The gcov run does not test SQLite because the -fprofile-args and -ftest-coverage options cause the compiler to generate different code. The gcov run merely verifies that the test suite provides 100% branch test coverage. The gcov run is a test of the test - a meta-test.

After gcov has been run to verify 100% branch test coverage, then the test program is recompiled using delivery compiler options (without the special -fprofile-arcs and -ftest-coverage options) and the test program is rerun. This second run is the actual test of SQLite.

It is important to verify that the gcov test run and the second real test run both give the same output. Any differences in output indicate either the use of undefined or indeterminate behavior in the SQLite code (and hence a bug), or a bug in the compiler. Note that SQLite has, over the previous decade, encountered bugs in each of GCC, Clang, and MSVC. Compiler bugs, while rare, do happen, which is why it is so important to test the code in an as-delivered configuration.

## 7.6. Mutation testing

Using gcov (or similar) to show that every branch instruction is taken at least once in both directions is a good measure of test suite quality. But even better is showing that every branch instruction makes a difference in the output. In other words, we want to show not only that every branch instruction both jumps and falls through but also that every branch is doing useful work and that the test suite is able to detect and verify that work. When a branch is found that does not make a difference in the output, that suggests that code associated with the branch can be removed (reducing the size of the library and perhaps making it run faster) or that the test suite is inadequately testing the feature that the branch implements.

SQLite strives to verify that every branch instruction makes a difference using mutation testing. A script first compiles the SQLite source code into assembly language (using, for example, the -S option to gcc). Then the script steps through the generated assembly language and, one by one, changes each branch instruction into either an unconditional jump or a no-op, compiles the result, and verifies that the test suite catches the mutation.

Unfortunately, SQLite contains many branch instructions that help the code run faster without changing the output. Such branches generate false-positives during mutation testing. As an example, consider the following hash function used to accelerate table-name lookup:

```
55  static unsigned int strHash(const char *z){
56    unsigned int h = 0;
57    unsigned char c;
58    while( (c = (unsigned char)*z++)!=0 ){     /*OPTIMIZATION-IF-TRUE*/
59      h = (h<<3) ^ h ^ sqlite3UpperToLower[c];
60    }
61    return h;
62  }

```

If the branch instruction that implements the "c!=0" test on line 58 is changed into a no-op, then the while-loop will loop forever and the test suite will fail with a time-out. But if that branch is changed into an unconditional jump, then the hash function will always return 0. The problem is that 0 is a valid hash. A hash function that always returns 0 still works in the sense that SQLite still always gets the correct answer. The table-name hash table degenerates into a linked-list and so the table-name lookups that occur while parsing SQL statements might be a little slower, but the end result will be the same.

To work around this problem, comments of the form "`/*OPTIMIZATION-IF-TRUE*/`" and "`/*OPTIMIZATION-IF-FALSE*/`" are inserted into the SQLite source code to tell the mutation testing script to ignore some branch instructions.

## 7.7. Experience with full test coverage

The developers of SQLite have found that full coverage testing is an extremely effective method for locating and preventing bugs. Because every single branch instruction in SQLite core code is covered by test cases, the developers can be confident that changes made in one part of the code do not have unintended consequences in other parts of the code. The many new features and performance improvements that have been added to SQLite in recent years would not have been possible without the availability of full-coverage testing.

Maintaining 100% MC/DC is laborious and time-consuming. The level of effort needed to maintain full-coverage testing is probably not cost effective for a typical application. However, we think that full-coverage testing is justified for a very widely deployed infrastructure library like SQLite, and especially for a database library which by its very nature "remembers" past mistakes.

# 8. Dynamic Analysis

Dynamic analysis refers to internal and external checks on the SQLite code which are performed while the code is live and running. Dynamic analysis has proven to be a great help in maintaining the quality of SQLite.

## 8.1. Assert

The SQLite core contains 6754 assert() statements that verify function preconditions and postconditions and loop invariants. Assert() is a macro which is a standard part of ANSI-C. The argument is a boolean value that is assumed to always be true. If the assertion is false, the program prints an error message and halts.

Assert() macros are disabled by compiling with the NDEBUG macro defined. In most systems, asserts are enabled by default. But in SQLite, the asserts are so numerous and are in such performance critical places, that the database engine runs about three times slower when asserts are enabled. Hence, the default (production) build of SQLite disables asserts. Assert statements are only enabled when SQLite is compiled with the SQLITE_DEBUG preprocessor macro defined.

See the Use Of assert in SQLite document for additional information about how SQLite uses assert().

## 8.2. Valgrind

Valgrind is perhaps the most amazing and useful developer tool in the world. Valgrind is a simulator - it simulates an x86 running a Linux binary. (Ports of Valgrind for platforms other than Linux are in development, but as of this writing, Valgrind only works reliably on Linux, which in the opinion of the SQLite developers means that Linux should be the preferred platform for all software development.) As Valgrind runs a Linux binary, it looks for all kinds of interesting errors such as array overruns, reading from uninitialized memory, stack overflows, memory leaks, and so forth. Valgrind finds problems that can easily slip through all of the other tests run against SQLite. And, when Valgrind does find an error, it can dump the developer directly into a symbolic debugger at the exact point where the error occurs, to facilitate a quick fix.

Because it is a simulator, running a binary in Valgrind is slower than running it on native hardware. (To a first approximation, an application running in Valgrind on a workstation will perform about the same as it would running natively on a smartphone.) So it is impractical to run the full SQLite test suite through Valgrind. However, the veryquick tests and the coverage of the TH3 tests are run through Valgrind prior to every release.

## 8.3. Memsys2

SQLite contains a pluggable memory allocation subsystem. The default implementation uses system malloc() and free(). However, if SQLite is compiled with SQLITE_MEMDEBUG, an alternative memory allocation wrapper (memsys2) is inserted that looks for memory allocation errors at run-time. The memsys2 wrapper checks for memory leaks, of course, but also looks for buffer overruns, uses of uninitialized memory, and attempts to use memory after it has been freed. These same checks are also done by valgrind (and, indeed, Valgrind does them better) but memsys2 has the advantage of being much faster than Valgrind, which means the checks can be done more often and for longer tests.

## 8.4. Mutex Asserts

SQLite contains a pluggable mutex subsystem. Depending on compile-time options, the default mutex system contains interfaces sqlite3_mutex_held() and sqlite3_mutex_notheld() that detect whether or not a particular mutex is held by the calling thread. These two interfaces are used extensively within assert() statements in SQLite to verify mutexes are held and released at all the right moments, in order to double-check that SQLite does work correctly in multi-threaded applications.

## 8.5. Journal Tests

One of the things that SQLite does to ensure that transactions are atomic across system crashes and power failures is to write all changes into the rollback journal file prior to changing the database. The TCL test harness contains an alternative OS backend implementation that helps to verify this is occurring correctly. The "journal-test VFS" monitors all disk I/O traffic between the database file and rollback journal, checking to make sure that nothing is written into the database file which has not first been written and synced to the rollback journal. If any discrepancies are found, an assertion fault is raised.

The journal tests are an additional double-check over and above the crash tests to make sure that SQLite transactions will be atomic across system crashes and power failures.

## 8.6. Undefined Behavior Checks

In the C programming language, it is very easy to write code that has "undefined" or "implementation defined" behavior. That means that the code might work during development, but then give a different answer on a different system, or when recompiled using different compiler options. Examples of undefined and implementation-defined behavior in ANSI C include:

- Signed integer overflow. (Signed integer overflow does not necessarily wrap around, as most people expect.)
- Shifting an N-bit integer by more than N bits.
- Shifting by a negative amount.
- Shifting a negative number.
- Using the memcpy() function on overlapping buffers.
- The order of evaluation of function arguments.
- Whether or not "char" variables are signed or unsigned.
- And so forth....

Since undefined and implementation-defined behavior is non-portable and can easily lead to incorrect answers, SQLite works very hard to avoid it. For example, when adding two integer column values together as part of an SQL statement, SQLite does not simply add them together using the C-language "+" operator. Instead, it first checks to make sure the addition will not overflow, and if it will, it does the addition using floating point instead.

To help ensure that SQLite does not make use of undefined or implementation defined behavior, the test suites are rerun using instrumented builds that try to detect undefined behavior. For example, test suites are run using the "-ftrapv" option of GCC. And they are run again using the "-fsanitize=undefined" option on Clang. And again using the "/RTC1" option in MSVC. Then the test suites are rerun using options like "-funsigned-char" and "-fsigned-char" to make sure that implementation differences do not matter either. Tests are then repeated on 32-bit and 64-bit systems and on big-endian and little-endian systems, using a variety of CPU architectures. Furthermore, the test suites are augmented with many test cases that are deliberately designed to provoke undefined behavior. For example: "SELECT -1*(-9223372036854775808);".

# 9. Disabled Optimization Tests

The sqlite3_test_control(SQLITE_TESTCTRL_OPTIMIZATIONS, ...) interface allows selected SQL statement optimizations to be disabled at run-time. SQLite should always generate exactly the same answer with optimizations enabled and with optimizations disabled; the answer simply arrives quicker with the optimizations turned on. So in a production environment, one always leaves the optimizations turned on (the default setting).

One verification technique used on SQLite is to run an entire test suite twice, once with optimizations left on and a second time with optimizations turned off, and verify that the same output is obtained both times. This shows that the optimizations do not introduce errors.

Not all test cases can be handled this way. Some test cases check to verify that the optimizations really are reducing the amount of computation by counting the number of disk accesses, sort operations, full-scan steps, or other processing steps that occur during queries. Those test cases will appear to fail when optimizations are disabled. But the majority of test cases simply check that the correct answer was obtained, and all of those cases can be run successfully with and without the optimizations, in order to show that the optimizations do not cause malfunctions.

# 10. Checklists

The SQLite developers use an on-line checklist to coordinate testing activity and to verify that all tests pass prior to each SQLite release. Past checklists are retained for historical reference. (The checklists are read-only for anonymous internet viewers, but developers can log in and update checklist items in their web browsers.) The use of checklists for SQLite testing and other development activities is inspired by The Checklist Manifesto.

The latest checklists contain approximately 200 items that are individually verified for each release. Some checklist items only take a few seconds to verify and mark off. Others involve test suites that run for many hours.

The release checklist is not automated: developers run each item on the checklist manually. We find that it is important to keep a human in the loop. Sometimes problems are found while running a checklist item even though the test itself passed. It is important to have a human reviewing the test output at the highest level, and constantly asking "Is this really right?"

The release checklist is continuously evolving. As new problems or potential problems are discovered, new checklist items are added to make sure those problems do not appear in subsequent releases. The release checklist has proven to be an invaluable tool in helping to ensure that nothing is overlooked during the release process.

# 11. Static Analysis

Static analysis means analyzing source code at compile-time to check for correctness. Static analysis includes compiler warning messages and more in-depth analysis engines such as the Clang Static Analyzer. SQLite compiles without warnings on GCC and Clang using the -Wall and -Wextra flags on Linux and Mac and on MSVC on Windows. No valid warnings are generated by the Clang Static Analyzer tool "scan-build" either (though recent versions of clang seem to generate many false-positives.) Nevertheless, some warnings might be generated by other static analyzers. Users are encouraged not to stress over these warnings and to instead take solace in the intense testing of SQLite described above.

Static analysis has not been helpful in finding bugs in SQLite. Static analysis has found a few bugs in SQLite, but those are the exceptions. More bugs have been introduced into SQLite while trying to get it to compile without warnings than have been found by static analysis.

# 12. Summary

SQLite is open source. This gives many people the idea that it is not well tested as commercial software and is perhaps unreliable. But that impression is false. SQLite has exhibited very high reliability in the field and a very low defect rate, especially considering how rapidly it is evolving. The quality of SQLite is achieved in part by careful code design and implementation. But extensive testing also plays a vital role in maintaining and improving the quality of SQLite. This document has summarized the testing procedures that every release of SQLite undergoes with the hope of inspiring confidence that SQLite is suitable for use in mission-critical applications.

This page was last updated on 2026-04-21 10:28:59Z