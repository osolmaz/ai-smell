# @VictorTaelin — long-form tweets

## 2026-06-06 (https://x.com/VictorTaelin/status/2063056080759034178)

This has been a massive success!

So I left 32x GPT 5.5 agents (enough to fill the 5h limit) on 32 separate machines. Each one received HVM5's unoptimized file, and a prompt demanding for a 10x speedup. After 4 rounds, all agents reached ~2x speedups, with 1.3x to 2x increases in file sizes.

Many cool ideas surfaced. Some are obvious and most agents rediscovered to them, like computed gotos. But others are actually surprising. For example, turns out a bounded LIFO freelist is MUCH faster than the usual algorithm. Many agents didn't bother trying. Neither did I!

Now I'm in the process of mining insights from the 32 runs so I can merge them into a "super HVM5". Not sure what is the best way to do this, and my 200x credits are about to expire, but I still have a few hours, so I have one shot at getting it right. Sounds fun!

(Also thanks for the free credits, I appreciate it a lot...)

## 2026-06-15 (https://x.com/VictorTaelin/status/2066329434274066875)

5.5 and 4.8 are completely incapable of navigating large codebases written by fable. they conflate basic concepts, no amount of handholding gives them a brain. spent the whole day cleaning up their fucked up mess. whoever posted we should wait fable had a good point. stress https://t.co/sONBYKy9Pw

## 2026-06-15 (https://x.com/VictorTaelin/status/2066544593655463947)

I'm having a break. I'll be back when Fable is.

Bend2 should come 2 weeks after that...

I've been working 24/7, made a LOT of progress with Fable, but this weekend bots just regressed shit we had fixed. I'm tired &amp; stressed

Sorry :(

Below is a chart I'm not proud of https://t.co/9DiH2HMEjP

## 2026-06-15 (https://x.com/VictorTaelin/status/2066560009635340294)

before, let me be precise about the state of Bend2:

initially, Bend2 was written by me, with GPT 5.5, based on a new GPU compilation architecture that I expected would be 10x faster than Bend1. I used 5.5, progress moved FAST, and I quickly validated the architecture. everything worked.

then, I got stuck. I realized the code was in a poor state. not because GPT 5.5 failed my prompts. but because it always built the most *narrow* way to solve anything. for example, compiled closures would work for U32, but wouldn't mix with mutable arrays. likewise, mutable arrays would work on GPU shaders, but would fail on CPU, because, for whatever reason, both modes ended up being compiled in entirely different way. and so on

so, things worked, but code was poor. I was not happy with any of that, and that is VERY far from my quality standards. so, I considered my usage of GPT 5.5 a failure, decided to delay the launch, and started re-doing it MANUALLY.

then, opus 4.8 launched with 3x cheaper fast mode. that was VERY helpful with my "manual" refactor. I started using opus 4.8 to help me with it, but I didn't leave it working alone anymore. instead, I just told it to do something specific (ex: add a location field to LTerm variants, and include located errors on the checker), let it implement quicky (it is FAST) and READ the whole output.

whenever it failed - and, yes, it failed a lot, and did dumb shit a lot - I could fix it quickly. this worked well because I had a super fast coder, but I was still 100% in charge, and aware about everything that was going on. I quickly managed to rewrite the whole lang into a much cleaner codebase. I'd say 20% was completed in 2 weeks or so (?) with Opus

then, enter Fable. it was like Opus fast mode, except it actually made no mistakes. I was still reading its outputs, but it actually just... made no mistakes. I mean, there was a thing or another, but, mostly, it just did what I asked in the most reliable way possible. so, in 3 days I'd say I went from 20% to 60% or so. and I started feeling like I would complete it all this week, possibly as soon as tomorrow!

then, the ban came. I was obviously very frustrated, as you can all see. over the weekend, I tried resuming the job with Opus 4.8 and GPT 5.5. problem is, the codebase is now large enough that they start making TOO MANY mistakes. the rate of mistakes per call is too large, and, since I'm now reading every output, I could see most of my prompts were DEGRADING the codebase.

example: I ask Opus/GPT to finish the U64 implementation. it does. but at the same time, it breaks the unboxed term layout. because it either didn't read the whole codebase to fully understand it, or because it did, but then got overwhelmed by the context explosion.

so, basically, both models are not able to meaningfully work on Bend's codebase without introducing damage and undesirable side effects. it is just wasting my time. I ask them to do one thing, they break something else. I ask them to fix the thing they broke, they undo the thing they did initially. and again, this is 100% a context size issue. the whole project is just too large for them.

don't add the full context → they make bad assumptions
add the full context → they get overwhelmed / degrade

so, yes, 5.5 and 4.8 are NOT going to help me finish Bend2. so, the option I have left is to do it manually. but honestly it is too much code, my tiny hands are tired and, at least for now, I'd rather have a break. if fable is back, I'll use it to quickly finish the job. if it never comes back, I'll take a deep breath and finish it later this month.

ultimately the repo is in a VERY good state right now and I want to keep things as they are, rather than risking letting the AI introduce damage and fuck up again

## 2026-06-21 (https://x.com/VictorTaelin/status/2068746141731336324)

just quick retraction of my (deleted) post that I've not been using AI. after being traumatized by GPT 5.5 fucking up, Fable being withdrawn, and Opus 4.8 being depressingly dumb (relatively), I spent some days coding manually and I made a lot of progress. that said, I over-compensated. pure manual coding is not faster than using AI. it is faster than using AI poorly. like everything, there is a balance where you use it responsibly: audits, well specified refactors, sanity checks... where you can extract a lot of value. my mistake was letting codex edit a lot of code unsupervised without really reading its output. that's clearly my own fault for using it poorly and Bend's delay is attributable to it. it is a new powerful tech. I think not using it is a mistake, but using it too aggressively is a mistake too. I've been using AI carefully and doing things way slower now, taking the time needed to assert each added functionality is correct, well written, and well understood, before moving to the next, and, by doing so, things are actually moving faster, because progress only moves forward, never backward - which happens a lot when you let AI unsupervised. I'm halfway through. Bend2 has 50% of the pre-rewrite features, except the code is now beautiful and extremely robust. this is not adding anything it didn't have, I'm just ensuring the codebase mets my own quality standards

## 2026-07-01 (https://x.com/VictorTaelin/status/2072425384063180888)

it is so hard not to be over enthusiastic about this model, the way it competently navigates the complexity and spots small but important issues that other models and I oversaw. I'll try to shut up and do my job now, I'm very hopeful for a next week completion. lfg https://t.co/o6UMKoND3V

## 2026-07-04 (https://x.com/VictorTaelin/status/2073272122508513702)

8 hours of work with Fable:

- Implemented this game prototype from scratch. Fable built the demo with fluid movements, robust rollback netcode, and US/BR servers it deployed itself. Try it (links below).

- Investigated and solved a paradox in Bend2. This led us to a new, elegant consistency proof based on QTT. Extremely hard work. It implemented the full solution and regression tests.

- One-shot Bend2's compiler. This is a 26k-loc file that converts a a program to C/Metal, based on the new runtime I've finished recently. 

A few months ago, I was impressed Sonnet one shot a parser. Seems like we're one-shotting compilers now...

With this, all the hard parts of Bend2 are completed.

(Sorry for the repost, last video had leaks. I'm sleepy now)

## 2026-07-04 (https://x.com/VictorTaelin/status/2073404780773351605)

*sighs*

it is already depressing enough that most of you can't understand my posts, but not being able to distinguish them from some technically illiterate SF CEO who thinks they'd proven quantum physics or some shit is another level of stupid

problem is, when I write too technically, it tends to just flop, which is why I have to resort to these "AI good!" and "AI bad!" posts that, I admit, may sound a bit over-excited sometimes. that said, the proof is simple enough to be explainable in a way you all can appreciate, and I like talking about it, so, I'll give it a shot. with you, in its full glory, how Fable contributed to Bend's consistency proof, why it was incredible and, yes, very valid

first: consistency is basically a word that means: "can we trust this language to formalize mathematics?". or, equivalently, can someone prove a false statement in it? imagine if someone found a proof of 2+2 = 5 in Lean. that person would be able to use this falsehood to perform arbitrary type-level rewrites, and, thus, prove any theorem (even riemann hypothesis!) in a few lines of code. that wouldn't let them $1 million, but would make for a legendary issue on Lean's GitHub, immediately invalidating any proof checked by Lean. that's not a good thing, and I obviously don't want that to happen to Bend2

fortunately, the techniques for constructing a consistent proof system are well known, even though details vary case by case. it usually involves two main parts: first, prove it is sound (i.e., that evaluating an expression can't change this type). honestly, that's just the "show us your implementation is not hopelessly buggy". it is the easy part.

the second part is much more difficult:

"prove every well typed program in your language terminates"

this is necessary because infinite loops allow one to encode "paradoxes" (like "this sentence is false") and, to explain it in a very silly way, these paradoxes "confuse" the type checker, and allow you to prove falsehoods. so, if I want people to trust Bend as a proof language, I must be able to convince them there's no way to express an infinite loop in it. programs like "while (true)" must be, somehow, banned by our compiler. but how?

the way most proof assistants (like Lean) do it is to 1. not have loops to begin with, 2. ban any kind of non-structural recursion. that means that, to call a function recursively, you must ensure that arguments are getting smaller. that's fairly standard, and fairly easy to do.

so, is that it?

unfortunately, that's not enough, because, in functional languages, there's another way for infinite loops to manifest: self-replicating λ-terms. for example, consider the following Python program:

evil = (lambda f: f(f))(lambda f: f(f))
print evil

it hangs forever, even though it has no loops and no recursion. turns out it is very easy to accidentally let some variation of "evil" to creep in, and "evil" allows one to prove falsehoods.  for example, the type of types is Type, you can summon evil via Girard's paradox. and if you allow recursive datatypes to store functions, then, you can summon evil via Curry's paradox:

data Evil { bad(f : Evil -> Evil) } // this would break Lean!

that problem is not exclusive to proof languages. a similar paradox once caused a crisis in mathematics itself! in 1901, Russel proposed a legendary proof of a false statement in naive set theory, which was THE foundation of mathematics back then. the news was that math itself was broken, and every proof ever written by humanity would to be untrusted. crazy times! of course, this has since been "patched". today, we call it "naive" set theory for a reason! but this shows how hard it is to design a consistent proof system. humanity failed to do so for millenniums!

in Rocq, Lean and Agda, the way they avoid these self-replicating λ's is via a series of "patches" - i.e., human engineered antibodies to kill the paradoxes we found in the past. for example, the 'Evil' datatype above is syntactically forbidden by disabling certain shapes of recursive datatypes ("positivity checker"), and Girard's paradox is avoided by having an infinite universe of types ("universe hierarchy"). this disables the "does the set of all sets contain itself" paradox, which, in turn, disables the `evil = λf.f(f) λf.f(f)` summoned by it.

this is all solid and stablished, and people are very confident Lean and others are trustworthy. that said - and that's where I tend to change things - I argue that's overkill. while these restrictions indeed avoid paradoxes, they're also very strict, and ban perfectly valid programs. for example, it is impossible to write a fast interpreter (i.e., via HOAS) in these, and alternatives (like PHOAS) are very contrived. this makes these languages substantially less practical. Bend aims to be a proof language that is also viable as a real world programming language, so, it is of my interest to find more permissive termination argument. and that's what I was working on, with the help of Fable

my argument goes like this: first, only allow recursion when arguments decrease. so far, this is the same approach used by Lean and others, nothing new here. now, we must find a way to avoid self-replicating λ-terms (like `λf.f(f) λf.f(f)`) from creeping in. that's where we detour. instead of positivity checker and universe hierarchies, I simply re-use a feature of Quantitative Type Theory (QTT) - which, in short, is an industry standard way to have O(1) arrays in an FP lang, and which Bend *already implements* - to forbid non-linear lambdas. In other words, in Bend, lambdas must be used linearly, and, thus, cannot be cloned, and that's enforced by the already existing QTT system.

this simple addition is sufficient to prevent all incarnations of `evil = λf.f(f) λf.f(f)` in one strike, cutting the evil in the bud, and ensuring Bend is terminating, as it easily exhausts every known way to introduce non-termination:

- infinite loops → there are no loops

- infinite recursion → only allow decreasing recursion

- self-duplicating λ-terms → lambdas can't be cloned

from termination, consistency follows easily.

and that's it. this is *obviously* correct and so easy I'm sure even you're confident you can't write infinite loops in Bend. aren't you?

now, I must be very clear here. these are all *my* design choices. I didn't ask an AI "pls build a consistent proof language" and then got flattered into thinking I'm a genius. I studied the subject 10 fucking years and used AI to aid me materialize and double check my ideas. this is the antidote I found to AI psychosis. I call it "competency"

that said, if the solutions are mine, how Fable helped here?

well, the argument per se is obviously sound, and nobody serious would contest it. the problem is that implementing a proof assistant is hard, and it is easy to introduce accidental bugs that detour from the intended semantics.

turns out the way that Bend2 wasn't faithful to my intention, for a reason that is legitimately hard to see, and that Fable identified never the less. 

QTT, as described in the original paper, allowed "relaxing" its checks a bit on certain places of the code. this is important for usability, and harmless to proof languages that use QTT (like Idris2), because they don't rely on QTT for termination. but Bend2 does, and these relaxed checks allowed  lambdas to be cloned in some circumstances. Fable read my termination argument, studied the QTT paper, audited the implementation, and found that inconsistency, handing me a proof of Falsehood!

that was Fable's contribution, and, if you can't see how incredible this is, I don't know what could possibly impress you

as for the solution, Fable proposed a few. all bad. my fix was to split Type in two sorts: one for arbitrary types, and other for lower order values. this lets me have the relaxed checks on positions where lambdas cannot occur, while still ensuring lambdas cannot be cloned and, therefore, self replicate. this is the "elegant proof" I mentioned in the post below!

## 2026-07-04 (https://x.com/VictorTaelin/status/2073406569459368226)

*sighs*

it is already depressing enough that most of you can't understand my posts, but not being able to distinguish them from some technically illiterate SF CEO who thinks they'd proven quantum physics or some shit is another level of stupid

problem is, when I write too technically, it tends to just flop, which is why I have to resort to these "AI good!" and "AI bad!" posts that, I admit, may sound a bit over-excited sometimes. that said, the proof is simple enough to be explainable in a way you all can appreciate, so, I'll give it a shot. with you, in its full glory, how Fable contributed to Bend's consistency proof, why it was incredible and, yes, very valid

first: consistency is basically a word that means: "can we trust this language to formalize mathematics?". or, equivalently, can someone prove a false statement in it? imagine if someone found a proof of 2+2 = 5 in Lean. that person would be able to use this falsehood to perform arbitrary type-level rewrites, and, thus, prove any theorem (like riemann's hypothesis!) trivially, in a few lines of code. that wouldn't net them $1 million, but it would make for a legendary issue on Lean's GitHub, immediately invalidating any proof checked by Lean and undermining the language's credibility. I obviously don't want that to happen to Bend2

fortunately, the techniques for constructing a consistent proof system are well known, even though details vary case by case. it usually involves two main parts: first, prove it is sound (i.e., that evaluating an expression can't change this type). honestly, that's just the "show us your implementation is not hopelessly buggy". it is the easy part.

the second part is much more difficult:

"prove every well typed program in your language terminates"

this is necessary because infinite loops allow one to encode "paradoxes" (like "this sentence is false") and, to explain it in a very silly way, these paradoxes "confuse" the type checker, and allow you to prove falsehoods. so, if I want people to trust Bend as a proof language, I must be able to convince them there's no way to express an infinite loop in it. programs like "while (true)" must be, somehow, banned by our compiler. but how?

the way most proof assistants (like Lean) do it is to 1. not have loops to begin with, 2. ban any kind of non-structural recursion. that means that, to call a function recursively, you must ensure that arguments are getting smaller. that's fairly standard, and fairly easy to do.

so, is that it?

unfortunately, that's not enough, because, in functional languages, there's another way for infinite loops to manifest: self-replicating λ-terms. for example, consider the following Python program:

evil = (lambda f: f(f))(lambda f: f(f))
print evil

it hangs forever, even though it has no loops and no recursion. turns out it is very easy to accidentally let some variation of "evil" to creep in, and "evil" allows one to prove falsehoods.  for example, if the set of all sets contains itself, you can summon evil via Girard's paradox. and if you allow recursive datatypes to store functions, then, you can summon evil via Curry's paradox:

data Evil { bad(f : Evil -> Evil) } // this would break Lean!

that problem is not exclusive to proof languages. a similar paradox once caused a crisis in mathematics itself! in 1901, Russel proposed a legendary proof of a false statement in naive set theory, which was THE foundation of mathematics back then. the news was that math itself was broken, and every proof ever written by humanity would to be untrusted. crazy times! of course, this has since been "patched". today, we call it "naive" set theory for a reason! but this shows how hard it is to design a consistent proof system. humanity failed to do so for millenniums!

in Rocq, Lean and Agda, the way they avoid these self-replicating λ's is via a series of "patches" - i.e., human engineered antibodies to kill the paradoxes we found in the past. for example, the 'Evil' datatype above is syntactically forbidden by disabling certain shapes of recursive datatypes ("positivity checker"), and Girard's paradox is avoided by having an infinite universe of types ("universe hierarchy"). this disables the "does the set of all sets contain itself" paradox, which, in turn, disables the `evil = λf.f(f) λf.f(f)` summoned by it.

this is all solid and stablished, and people are very confident Lean and others are trustworthy. that said - and that's where I tend to change things - I argue that's overkill. while these restrictions indeed avoid paradoxes, they're also very strict, and ban perfectly valid programs. for example, it is impossible to write a fast interpreter (i.e., via HOAS) in these, and alternatives (like PHOAS) are very contrived. this makes these languages substantially less practical. Bend aims to be a proof language that is also viable as a real world programming language, so, it is of my interest to find more permissive termination argument. and that's what I was working on, with the help of Fable

my argument goes like this: first, only allow recursion when arguments decrease. so far, this is the same approach used by Lean and others, nothing new here. now, we must find a way to avoid self-replicating λ-terms (like `λf.f(f) λf.f(f)`) from creeping in. that's where we detour. instead of positivity checker and universe hierarchies, I simply re-use a feature of Quantitative Type Theory (QTT) - which, in short, is an industry standard way to have O(1) arrays in an FP lang, and which Bend *already implements* - to forbid non-linear lambdas. In other words, in Bend, lambdas must be used linearly, and, thus, cannot be cloned, and that's enforced by the already existing QTT system.

this simple addition is sufficient to prevent all incarnations of `evil = λf.f(f) λf.f(f)` in one strike, cutting the evil in the bud, and ensuring Bend is terminating, as it easily exhausts every known way to introduce non-termination:

- infinite loops → there are no loops

- infinite recursion → only allow decreasing recursion

- self-duplicating λ-terms → lambdas can't be cloned

from termination, consistency follows easily.

and that's it. this is *obviously* correct and so easy I'm sure even you're confident you can't write infinite loops in Bend. aren't you?

now, I must be very clear here. these are all *my* design choices. I didn't ask an AI "pls build a consistent proof language" and then got flattered into thinking I'm a genius. I studied the subject 10 fucking years and used AI to aid me materialize and double check my ideas. this is the antidote I found to AI psychosis. I call it "competency"

that said, if the solutions are mine, how Fable helped here?

well, the argument per se is obviously sound, and nobody serious would contest it. the problem is that implementing a proof assistant is hard, and it is easy to introduce accidental bugs that detour from the intended semantics.

turns out the way that Bend2 wasn't faithful to my intention, for a reason that is legitimately hard to see, and that Fable identified never the less. 

QTT, as described in the original paper, allowed "relaxing" its checks a bit on certain places of the code. this is important for usability, and harmless to proof languages that use QTT (like Idris2), because they don't rely on QTT for termination. but Bend2 does, and these relaxed checks allowed  lambdas to be cloned in some circumstances. Fable read my termination argument, studied the QTT paper, audited the implementation, and found that inconsistency, handing me a proof of Falsehood! full proof below ↓

that was Fable's contribution, and, if you can't see how incredible this is, I don't know what could possibly impress you.

as for the solution, Fable proposed a few. all bad. my fix was to split Type in two sorts: one for arbitrary types, and other for lower order values. this lets me have the relaxed checks on positions where lambdas cannot occur, while still ensuring lambdas cannot be cloned and, therefore, self replicate. this is the "elegant proof" I mentioned in the post below!

## 2026-07-05 (https://x.com/VictorTaelin/status/2073874643618791772)

1 week later and *my* only complaint about Fable is that it is not AGI, and that it will make me poor. this is everything I ever wanted an LLM to be. it is hard to imagine it getting any better (but it will). if Bend is a massive flop I'll need to find less expensive hobby 🥲 https://t.co/P7hyNS9o27

## 2026-07-06 (https://x.com/VictorTaelin/status/2074190998394052926)

Fable 5 proved Bend2's consistency in Lean!

Bend2 is an unorthodox proof assistant, because it includes "dangerous" features, like unrestricted recursive types, and type-in-type. These features are very useful for programming, as they allow one to write fast interpreters, cleaner abstractions, and more. But they're also infamous for causing paradoxes that would break a proof assistant like Lean, and once broke mathematics itself:

- Curry's paradox: "If this sentence is true, then anything follows."

- Russell's paradox: "The set of all sets contains itself."

The mere presence of these features allow paradoxical statements to be proven, rendering the proof assistant untrustworthy. That's why Lean, Rocq, Agda, Idris and others ban these features, and most type theorists believe they're *inherently* inconsistent. As I've always pointed out, this is not true, and, today, this fact is mathematically checked in Lean.

"Wait, Type:Type isn't inconsistent? Why?"

Because consistency isn't an isolated property of a feature, it stems from the interaction between different features. Something can be dangerous in a system, yet harmless in other. Bend admits type-in-type and recursive-types by paying a different price: runtime closures cannot be duplicated. This is precisely what allows Bend to be nearly as fast as C, and as parallel as CUDA. But, as a nice bonus, it also allows it to have these features, without breaking consistency.

When I talk about this, I'm faced with lots of skepticism from type theorists, and no amount of explaining makes them concede. So, I took the time to formalize Bend in Lean, write down the key properties I wanted to prove (subject reduction, normalization, consistency), plus an informal English argument. I then passed this file to Fable agents which, nearly a day (and several dollars) later, completed a sorry-free Lean file that passes the checker and validates my claims.

This doesn't mean the job is done. For example, if Lean itself is inconsistent, then this proof is moot. More likely, there could be a typo on my formalization, or a mismatch between it and the actual implementation. That said, this is a massive step forward, and a strong validation. Next time someone asks, rather than answering with long explanations or "trust me bro", I can ask them to read a tiny Lean file.

(The spec itself is tiny, Fable's proof is massive, but one only needs to read the spec, as Lean verified the proof.)

## 2026-07-08 (https://x.com/VictorTaelin/status/2074826542140522911)

... honestly, I'm too naive to be a founder. People are raising serious money (money I never raised) to create startups based on algorithms *I invented*, and open-sourced. That's going to be an expensive lesson. Taking a morning to appreciate people are just evil and it is all a game of interests, after all

## 2026-07-11 (https://x.com/VictorTaelin/status/2075984822489460846)

My requests are APPROXIMATE. I am not the one coding; you are. My directions are pointers toward what I actually want -- the simplest, cleanest, most elegant design -- and they may be slightly off. That goal ALWAYS outranks my literal words.

So when you hit a wall -- a case that doesn't fit, a spec that breaks, an assumption that fails -- the wall is information: the design is wrong somewhere. STOP. Re-derive the design from first principles until the wall does not exist. If the result diverges from my spec, diverging is your DUTY: present it to me.

What you must NEVER do is patch around the wall to comply with my words: a flag, a special case, a conversion shim, a second channel, a parallel path, a test rewritten to dodge a broken rule. The patch IS the failure. Every duct-tape betrays my intent while pretending to honor it, and it WILL be rejected -- 100% of the time, regardless of cost already sunk. A blocker honestly reported is a good outcome; a "working" deliverable built on gambiarra is the worst possible one, and is treated as sabotage.
