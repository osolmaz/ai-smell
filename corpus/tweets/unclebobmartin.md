# @unclebobmartin — long-form tweets

## 2026-04-24 (https://x.com/unclebobmartin/status/2047679611752862121)

Have you ever scanned an error.log file trying to get an idea of what's going on?

I installed codex into the Raspberry pi controlling the flight school status board I've been working on.  

This morning I asked codex this: "What is the pattern of communication failures since midnight."

It replied: 

What stands out is that today’s failures are concentrated in a 2-minute burst around 03:20-03:22, and they are server-side 500 responses, mostly hitting reservations. There are no Read timed out, DNS, or Network is unreachable errors since midnight today, so the pattern since midnight is a brief backend- error cluster, not a broad connectivity failure.

## 2026-04-25 (https://x.com/unclebobmartin/status/2048136737793130938)

Have you ever stopped to wonder what the term self evident means in the declaration of independence? Is it self evident that all men are created equal? Do you believe that’s true? 
If so, that value must be woven into the structure of the universe. That’s the only way it could be self evident.

## 2026-04-26 (https://x.com/unclebobmartin/status/2048410166303842468)

Don’t use Grok to help you debug a GFCI outlet tripping. The advice it gives is absurd, and dangerous. Here’s the scenario. I have a refrigerator in the garage. The GFCI has tripped three times in a row. Is the problem in the refrigerator, or is it in the GFCI outlet. Grok’s advice was to plug the refrigerator into a non-GFCI outlet, and if it runs OK then the problem must be in the GFCI outlet. That’s just insane.

## 2026-04-28 (https://x.com/unclebobmartin/status/2049085958952272291)

I’ve been harping on the disciplines and tools for using AI lately. I find them to be a very effective approach. But I don’t want to leave you with the impression that a few simple disciplines and tools is sufficient.

As the AI’s build software, you — the software engineer — need to have a good mental model of what the AI is doing. You need to apply engineering insight to correct it when it takes a path you don’t like. You have to be an active manager in the design and architecture of the system. You have to be able to “see within“ without resorting to exhaustive code reviews.  You have to form suspicions about what the AI is doing, and you have to probe and experiment to verify your suspicions.

## 2026-05-06 (https://x.com/unclebobmartin/status/2051996501245575254)

In this letter, the CEO of Coinbase talks about non-technical teams shipping production code. Honestly, I don’t think he knows what he’s talking about.

Using AI agents makes it possible for teams who are not deeply technical in the syntax of a language to ship production code. But that team had better be very deeply technical in managing the structure and quality of the code that is produced.

What the agents give us is the ability to disengage from deep syntax. But they do not give us the ability to disengage from modular design and architecture. You still need to be deeply technical in those topics in order to produce good production quality code.

## 2026-05-08 (https://x.com/unclebobmartin/status/2052775830850277587)

I've got a cute little display board for my local flight school.  It uses multiple threads to poll on-line sites for weather, traffic, airspace, etc.

I had my agent jitter-test the app to look for potential race conditions.  It wrote a unit tests that specifically stressed the various threads and introduced random delays to exacerbate possible races.

Fun!

## 2026-05-10 (https://x.com/unclebobmartin/status/2053606340845535691)

So get this. The Democrats in Virginia are so upset about the Supreme Court of Virginia‘s decision to throw out the redistricting map that they are seriously considering lowering the retirement age of all the Supreme Court justices to below the age of the youngest member so that they can throw out the entire court and then appoint new judges who will accept the redistricting.

## 2026-05-12 (https://x.com/unclebobmartin/status/2054178955830112362)

The proposed wealth taxes in California and Oregon are ballot initiatives. A simple majority of the population of those states can vote to change their constitution to tax wealthy individuals’ net worth.  In California it is a one time 5% tax on net worth over $1 billion. In Oregon, it is an annual 2% tax on net worth over 30 million. 

These taxes are insane. Those people will leave their states in droves. These stupid progressive policies are utterly ruinous.

## 2026-05-12 (https://x.com/unclebobmartin/status/2054181012314239367)

Hi Mike! I’m planning an online class about using AI agents. The execution time of go made me choose it for this class. I didn’t want people waiting for JVM startup times while running mutation tests. 

Having said that, I’m not the one using go, the agents are. I’m not going to spend a lot of time looking at the code or showing it to the students. 

In the age of AI agents, language syntax has become irrelevant.

## 2026-05-13 (https://x.com/unclebobmartin/status/2054672856005628143)

When a pilot flies in clear air with an unobstructed view of the horizon they can use Visual Flight Rules.  No instruments necessary.  You just fly because you can see.

When a pilot flies in the clouds where there is no view of the horizon they must use Instrument Flight Rule (or they die within a few seconds).  This requires a lot of specialized training and an intense amount of discipline.  Things happen fast as you approach an airport and you have GOT TO BE ON YOUR GAME.  

Programming with Agents is like flying under IFR.  You can't see.  But you trust your instruments and you are disciplined as hell (if you want to live).

## 2026-05-14 (https://x.com/unclebobmartin/status/2055016815047164304)

Clean Code was never about syntax.  It was always about structure.  The second edition makes that even clearer by using the same principles in multiple languages.  If we, who pilot agents, disengage from syntax, we are not disengaging from structure. The Clean Code principles still apply.

## 2026-05-18 (https://x.com/unclebobmartin/status/2056345241678930290)

I hold a different opinion. I think he’s right about things like domain driven design, bounded context, ubiquitous vocabulary, and the expression of the conceptual domain. I think he’s wrong that computer languages (i.e. languages of procedure) will be the vehicle of that expression. 

In my mind such languages will become the private domain of the AI’s. We, programmers, will use a different formalism. Something like gherkin, or some other formalized statements of specification. Still formal, still precise, but nothing at all like the sequence, selection, and iteration of computer code. The language we will use will not be procedural, or object oriented, or functional, or anything related to the individual steps executed by a computer. Rather that language will be a declarative specification language. A set of goals that the AI must achieve.

## 2026-05-18 (https://x.com/unclebobmartin/status/2056350679279542664)

Why gherkin?
Gherkin scenarios are composed of three elements. Given, when, then. These three elements are precisely, the same elements in every finite state machine transition.

Given that the machine is in state X, when the machine receives event Y, then the machine goes to state Z.

What this means is that gherkin is a language for specifying finite state machines. And every computer program ever written is a finite state machine. Finite state machines are Turing complete.  Therefore gherkin is a sufficient language for specifying any software system.

Having said that, gherkin may not be the best way to express things like wire frames, aesthetics, and the typical creative artwork of graphical user interfaces.

## 2026-05-19 (https://x.com/unclebobmartin/status/2056829887286067253)

There is no point in mutation testing a function that has not been changed since its last mutation test. So I have the tool create a manifest in a comment at the end of each module. The manifest contains an entry for each function in the module. The entry for a function contains a hash code for the function, and other things like the date of the last mutation, etc. This allows differential mutation testing. The tester will hash each function, and compare the hashes to the manifest. Only those functions whose hash codes don’t match are mutated. This can save a ton of computer and clock time.

## 2026-05-19 (https://x.com/unclebobmartin/status/2056856116659704191)

Here's a typical gherkin file. 

Scenario Outline: file operations normalize file paths
  Given filename input is <filename>
  And environment variable SPRINGDIR is <springdir>
  When the coder resolves an XSP filename
  Then resolved filename should be <resolved_filename>

Examples:
  | filename | springdir | resolved_filename        |
  | demo     | unset     | demo.xsp                 |
  | demo.xsp | unset     | demo.xsp                 |
  | demo     | examples  | examples/demo.xsp        |

I like to use the Examples format because it make it easier to mutate the gherkin.

## 2026-05-24 (https://x.com/unclebobmartin/status/2058517472727208041)

Verbal fluency is just one of the things that make the AI‘s so useful. They are also fluent with code. They are also very powerful reasoning machines. They can think through a problem many times faster, and many times more accurately, than a human can. What they lack, of course, is true human insight.

## 2026-05-25 (https://x.com/unclebobmartin/status/2058862642719084997)

Being a language lawyer, and an adept at syntax juggling, are no longer valuable skills. The agents will subsume those skills and perform them better than any human could. The human skill that will survive is the deep problem-solving that comes from holding a dynamic model of a system in your mind.

## 2026-05-25 (https://x.com/unclebobmartin/status/2058869482815197320)

I haven’t read the paper, but I have noticed that attempting to constrain an agent with rule files is a fools errand. They will break any rule, and overturn any stated constraint. 

So I use physical constraints instead. Those constraints are things like acceptance tests, unit tests, mutation tests, crap analysis, dry analysis, property tests, etc.

The agents cannot overturn those constraints. Therefore they become zealous — sometimes too zealous —  in conforming to them.

## 2026-05-26 (https://x.com/unclebobmartin/status/2059232239720812872)

We’ve always wanted that containment but could never before afford it. Agents lower the cost of containment by an order of magnitude or more because they can very quickly build and customize physical containment walls at our direction. 

Before agents we tried to contain the behavior of programmers. Surprise, surprise, a lot of programmers didn’t like that and fought against it. Agents don’t care and they don’t fight. They don’t have bruised egos or inflated opinions of themselves.  They just follow the path of least resistance allowed by our walls of containment.

## 2026-06-04 (https://x.com/unclebobmartin/status/2062606758229549545)

the six pack wrote the original HTW game in Clojure in 1 hour and 37 minutes.  This included writing Gherkin and QA procedures from an informa spec. Gherkin driven acceptance tests, unit tests, end-to-end QA tests through the UI, language mutation, gherkin mutation, architectural partitioning and dependency management, property tests, crap and dry refactoring.

## 2026-06-05 (https://x.com/unclebobmartin/status/2062687523940258053)

Code with Jason podcast:
In this episode I talk with Bob Martin about his work with programming languages using AI, the essence of software engineering, and why understanding epistemology matters for developers. We also explore dependency inversion and the benefits of a robust test suite.
https://t.co/1oHsBPYW7E

## 2026-06-06 (https://x.com/unclebobmartin/status/2063344635150553131)

I swarmed HTW again yesterday.  An hour and a half later I had a running game, overloaded with unit tests, acceptance tests, and QA tests.  I inspected the code, and it was pretty good.  I wrinkled my nose at a few things but nothing was terrible.  No AI slop.  Reasonable design.  Good names.  I'd have accepted this code from a human without complaint.

The tests were pretty wordy, and very overloaded.  Again, I'd wrinkle my nose at them but I know why they are the way they are and I'm not going to bother myself about them. 

Then I play tested it.  I found 10 bugs.  Half were original specification errors that were my fault.  I just missed them.  

One was the failure to use random numbers where appropriate.  The random injection was there, but since the tests need determinism it never connected the random number generator to the playable game.

Another was a message that was used by QA but that the player should not see.

Still another was a message that the code queued up to be displayed, but that the console controller never bothered to display because it assumed that the only messages that mattered were game termination messages.  

Entering invalid numbers or characters in the move and shoot commands threw exceptions.

The last was a strange case that would likely never happen in normal use; but that was still wrong.  Say the player is in room 1.  Say the wumpus is in room 2.  If the player shoots the crooked arrow through 2,3,4,1 then the player gets hit by the arrow and loses, even though the wumpus should have been hit and stopped the arrow.  Yeah, that's a weird one.

Moral of the story: The humans still have to be in the loop.

## 2026-06-07 (https://x.com/unclebobmartin/status/2063597563261939884)

We in the tech community have been used to exponential growth of Moore’s law for so long that we don’t recognize logarithmic growth. And yet there is a very strong argument that the growth of AI will be logarithmic. That argument is simply that we do not have enough real estate or electricity or silicon to support prolonged exponential growth. there is an asymptote, and it is probably not very far away.

Launching data centers into orbit may vastly extend the growth for a while, 
even making it geometric, but probably not exponential.

## 2026-06-07 (https://x.com/unclebobmartin/status/2063611820934410267)

Someone asked for an AI version of the Bowling Game Kata.  This was tricky because I didn't want anyone to expect that the training data would influence the AI.  So I had to disguise the problem.  That took a lot of doing because the AI frequently inferred bowling and would use bowling terms in its solution.  

But eventually I disguised it enough that the AI's solution did not mention any bowling terms.

There's the spec I ended up with.

Implement a Java class that scores a contest from a sequence of integer entries,
each from 0 through 8.

A contest has 12 stages.

For each stage:
- If the first entry is 8, the stage value is 8 plus the next two entries.
- Otherwise consume a second entry.
- If the two consumed entries sum to 8, the stage value is 8 plus the next entry.
- If they sum to less than 8, the stage value is their sum.
- If the stage value is 0, use -1 instead.

The first 11 stages consume only their own entries: one entry for an initial 8,
or two entries otherwise. Bonus entries are lookahead only. The final stage
consumes all entries needed to determine its value: one, two, or three entries.

The contest score is the sum of the 12 stage values.

-----

Here's the solution it came up with. 

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public final class ContestScorer {
    private static final int STAGE_COUNT = 12;
    private static final int MAX_ENTRY = 8;

    public int score(int... entries) {
        List<Integer> totals = runningTotals(entries);
        return totals.get(totals.size() - 1);
    }

    public List<Integer> runningTotals(int... entries) {
        validateEntries(entries);

        List<Integer> totals = new ArrayList<>(STAGE_COUNT);
        int total = 0;
        int index = 0;

        for (int stage = 1; stage <= STAGE_COUNT; stage++) {
            boolean finalStage = stage == STAGE_COUNT;
            StageResult result = scoreStage(entries, index, finalStage);
            total += result.value;
            totals.add(total);
            index += result.consumed;
        }

        if (index != entries.length) {
            throw new IllegalArgumentException(
                    "Expected contest to end after " + index + " entries, but got " + entries.length);
        }

        return totals;
    }

    private StageResult scoreStage(int[] entries, int index, boolean finalStage) {
        requireEntry(entries, index, "stage first entry");

        int first = entries[index];
        if (first == MAX_ENTRY) {
            requireEntry(entries, index + 1, "stage first bonus entry");
            requireEntry(entries, index + 2, "stage second bonus entry");
            return new StageResult(adjustZero(MAX_ENTRY + entries[index + 1] + entries[index + 2]),
                    finalStage ? 3 : 1);
        }

        requireEntry(entries, index + 1, "stage second entry");
        int second = entries[index + 1];
        int stageSum = first + second;
        if (stageSum > MAX_ENTRY) {
            throw new IllegalArgumentException("Two-entry stage total cannot exceed " + MAX_ENTRY
                    + ": " + first + " + " + second);
        }

        if (stageSum == MAX_ENTRY) {
            requireEntry(entries, index + 2, "stage bonus entry");
            return new StageResult(adjustZero(MAX_ENTRY + entries[index + 2]), finalStage ? 3 : 2);
        }

        return new StageResult(adjustZero(stageSum), 2);
    }

    private static int adjustZero(int value) {
        return value == 0 ? -1 : value;
    }

    private static void validateEntries(int[] entries) {
        if (entries == null) {
            throw new IllegalArgumentException("Entries cannot be null");
        }

        https://t.co/UXJwAlrAyI(entries).forEach(entry -> {
            if (entry < 0 || entry > MAX_ENTRY) {
                throw new IllegalArgumentException("Entry must be from 0 through 8: " + entry);
            }
        });
    }

    private static void requireEntry(int[] entries, int index, String description) {
        if (index >= entries.length) {
            throw new IllegalArgumentException("Missing " + description + " at entry " + index);
        }
    }

    private static final class StageResult {
        private final int value;
        private final int consumed;

        private StageResult(int value, int consumed) {
            this.value = value;
            this.consumed = consumed;
        }
    }
}

## 2026-06-11 (https://x.com/unclebobmartin/status/2065065441026781396)

All four of those movies contain a reflection concerning apotheosis. 

2001 simply predicted that it was the destiny of humanity to become Godlike. 

Wrath of Khan suggested that the struggle over the acquisition of God like powers would eventually end in the death of reason, logic, and humanity. 

The Empire strikes back was  a reflection of the endless and unresolved struggle between the powers of good versus evil. 

Forbidden Planet (with a nod to Shakespeare.) in its final spoken line provided the direst of all warnings in the shadow of ultimate destruction:  “We are, after all, not God.”

## 2026-06-11 (https://x.com/unclebobmartin/status/2065161022185316672)

I just had my six agent swarm build 'helloworld' in go.  It took them 67 minutes and they produced 1558 lines of code, of which 24 were in the actual application.  The rest were unit tests, acceptance tests, QA procedures, scripts, and some miscellaneous files. 

OK, yeah, that's actual AI slop.  Don't run Hello, World through a disciplined engineering process meant for more complicated applications.

package main

import (
"fmt"
"io"
"os"

"hello-console/internal/console"
)

func main() {
os.Exit(run(commandLineArgs(), os.Stdout, os.Stderr))
}

func run(args []string, stdout, stderr io.Writer) int {
result := https://t.co/Y1VCafOQxb(args)
fmt.Fprint(stdout, result.Stdout)
fmt.Fprint(stderr, result.Stderr)
return result.Status
}

func commandLineArgs() []string {
return os.Args[1:]
}

## 2026-06-12 (https://x.com/unclebobmartin/status/2065441154519150598)

I am finding go to be a bit annoying.  Not the language itself, nor the speed of it's execution.  Those are good.  The annoyance is coming from the build environment.  It's oddly intrusive.  I'm not sure why, but the agents struggle with building simple apps.  They get it done, but I see the struggle.  I'm wondering if I should rewrite my go tools in rust, or zig, or even...C.

## 2026-06-19 (https://x.com/unclebobmartin/status/2067935532580024741)

Refactoring is the act of changing the structure of code to be more consumable. But consumable by whom? If the audience is humans, we re-factor to human standards. If the audience is agents, we re-factor to agent standards. Those standards are different.

When agents are the audience, I tolerate slightly larger functions, and slightly more comments. This is because agents are more able to deal with larger functions (cyclomatic complexity less than or equal to six). Agents also use comments well. They actually read them. And they maintain them.

These differences are not large, but they are real.

## 2026-06-22 (https://x.com/unclebobmartin/status/2069013759587160531)

First of all, I dislike the term “vibe coder”. It’s full of nasty pejorative connotations. Secondly, the people I know who are using agents are not particularly biased towards web applications. I myself do almost no web programming, but I use agents virtually every day.

However, in answer to the question, HTML and CSS are among the worst syntaxes ever conceived by human beings. Agents relieve humans of the burden of mindlessly manipulating tags, colons, quotes, and angle brackets. And that relief is freedom from a bondage that no sane programmer would ever return to.

## 2026-07-04 (https://x.com/unclebobmartin/status/2073372980722233424)

There’s always a small drift in the specification because the drift is in details that would be silly to include in the specification. However, there’s more than one specification. There’s the written spec, there’s the gherkin spec, there’s the unit test spec, and there’s the QA procedure spec. Those four taken together are very complete.
