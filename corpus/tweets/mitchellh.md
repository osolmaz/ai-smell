# @mitchellh — long-form tweets

## 2026-05-07 (https://x.com/mitchellh/status/2052397933522506079)

AI slop is good, actually. Slop is what enables fast parallel experimentation. The etiquette and skill is understanding the boundaries of where slop exists and the extent to which it should be cleaned up and how.

A few examples:

I’m working on the internals of some system right now. The API and GUI of this thing is fully zero shame slop. It’s horrible. But it lets me focus on the core quality while shipping a usable piece of alpha quality software to testers (transparent about the slop frontend). 

Similarly, this system has plugins. We sent agents in Ralph loops overnight to generate dozens of plugins. The plugins are slop. The quality is bad. The plugin API/SDK is absolutely not done.

But we can test a full GUI with a full plugin ecosystem. When we change the API, we can regenerate them all. The cost of change is just tokens, the velocity is incomparable to before.

I built Terraform. We tested and shipped TF 0.1 with about 3 very weak providers. Because we ran out of time. Building was slow. And when we changed our SDK the cost was immense. Totally different today, 10 years later. Today, I would’ve slop generated 100 providers (again, with transparency and cleanup later, but just to prove it out).

As an anti example, I would not PR this (without prior warning) to another project. I would not throw this onto customers without full review or transparency (as I’m already doing). I would not accept first pass slop. It’s almost never right. 

Slop is a tool. And like anything else it’s not blanket bad or good. The context is everything.

## 2026-05-20 (https://x.com/mitchellh/status/2057229385963618787)

This is why PR diff speed matters. This isn't a dunk on GitHub specifically, because GitLab, Forgejo, etc. are all equal or worse. But this is the kind of thing that drives me nuts, because this is a core workflow and its slow enough I literally take my hands off the keyboard.

Btw, when my mouse jiggles on the left, its because the page is literally skipping frames and I'm instinctively shaking my mouse to see if it'll respond. And on the keyboard input you can literally here me finish typing before a letter even shows up. 

For someone like me who is an expert at these tools, my brain navigates the tool dramatically faster than it can keep up, and that is not good. The tool should not get in the way.

## 2026-05-26 (https://x.com/mitchellh/status/2059376793837350966)

Here's the ATC audio clip of my final landing ever. From humble beginnings in a DA40 to ~600 hours in a Vision Jet at 31,000 feet, I love to fly. Due to my growing personal and professional obligations, my final and best ADM decision as a PIC was to stop. 

This was my toughest landing. The skies were clear. The wind was straight down the runway. It's my home field I've landed at hundreds of times. But I knew it was my last.

You can't hear it in the clip but my voice felt shaky. I'm doing my best to focus on a safe landing but I knew that was the last "cleared to land" readback I'd ever give. The landing was smooth. I parked the jet, locked her up, and gave her one last pat on the nose. We had good times.

I'm no longer a pilot.

Locking in for what's next.

🫡

## 2026-05-27 (https://x.com/mitchellh/status/2059758320966312206)

As the family IT guy its so disappointing how bad of an experience technology is for non-technical people. 

I had the distinct pleasure of building educational software for kids full time for a summer while in college (s/o to @WilliamsonMark), and I remember they did weekly/biweekly user testing where a group of toddlers would come in and we'd record them using the software in various states and then adjust accordingly.

Every single session was SHOCKINGLY illuminating. Like, I expected after a number of these I'd empathize more and build better toddler software one-shot right? Hell fucking no. Every user study was so educational. I learned I simply can't enter the mind of a toddler.

Do TV companies, Netflix/Roku/etc. do user studies with elderly people? Do they realize how dogshit and impossible to navigate their interfaces are? 

Asking some elderly family members to "sign up and schedule an Uber to pick you up for the airport" is like mission impossible. I thought they were exaggerating, then I tried the experience and holy shit man. Try cold finding, installing, signing up, and scheduling an Uber on a 5 year old iPhone with max font size. Its insane.

## 2026-06-03 (https://x.com/mitchellh/status/2062199823311499391)

My teeth were clenched, but Tesla FSD just reversed out of my garage through a curved driveway with less than 2 inches of clearance on either side with a brick wall and my wife’s SUV.  Crazy work.

I knew it’s possible cause I do it regularly. But it’s a lot of work, a lot of adjustment cause you have that 2 inch clearance through a curve. 

I started today and was like, you know what, I’m tired this morning. I’m going to let Jesus take the wheel. And it did it. So my mornings are about to become significantly more chill. 

I have a video but don’t want to dox myself so can’t share lol.

## 2026-06-10 (https://x.com/mitchellh/status/2064773611647574429)

Fable is a good model. As with all new models, it is simultaneously excellent and entirely unremarkable (relative to other models). It is slow and expensive, and the "loops are all you need" discourse they are pushing is obvious in the context of someone using Fable-class models

What I've found so far is that for broad scope design (code architecture) tasks, Fable is unremarkable. Or, not better enough to justify its cost and speed.

But in highly targeted goal-oriented loops, it is another beast entirely. It is very slow but produces very good results. 

I let it churn on optimizing a SwiftUI-layout resolver in Go I wrote and it was able to bring it down to an order of magnitude I could not reach myself (micro => nanosecond scale). But it took 2 hours and $40 to do it and I had to claw back some changes it overfit to Apple Silicon. Still, very worth it.

In comparison, for "implement this feature/change" iterative work, I ran head-to-head Fable vs GPT5.5 vs. GLM-5.1. They all produced equally acceptable final results, but GPT5/GLM did it in a couple minutes and Fable was churning away for 40 minutes. And GLM cost me less than a dollar, GPT5.5 ~$1.50, and Fable cost $9.

You can see that in this context, interactively working with an agent is nonsense. Its too slow. You need to write loops to keep the agent working and you probably want to highly parallelize the work being done. As with all things, I think a balance makes sense...

My sense is that I'd reserve Fable for targeted, surgical analysis and work. Not for daily driving everyday tasks. 

I'm going to keep spending a shitload of money (relatively) and maining Fable for the rest of the week to continue to judge, will report if anything changes. I'll continue to head-to-head as well.

## 2026-06-15 (https://x.com/mitchellh/status/2066543431435051086)

Yep. Said no to $50 million, the 150, then 300, then 5 billion. Ultimately my company got sold for 6 and some change (billion). If someone is offering you money it’s usually because you’re doing something right and you’re in the best position to know whether to take it or not.

Full respect to founders whenever they choose to sell, not saying to hold. Just saying the number alone tells you nothing and looking at only the number is not the right move.

## 2026-06-15 (https://x.com/mitchellh/status/2066544428597268878)

Also, sold my first business fully bootstrapped in college for $200K (back in 2009ish when I was 19!). It had more growth potential but I took the $200K and it gave me the stability and funding to start my next thing which ended up being the multi-billion dollar thing. 

I could’ve taken that first idea I think to millions… but saw the next as a bigger opportunity. So dumped it early and went into the 10 year big bet journey. Paid off luckily, could’ve easily not. But just another example of the bigger picture around dollar amounts and dollars as just one data point of many.

## 2026-06-16 (https://x.com/mitchellh/status/2066960258304782598)

We've gone really quickly from "local models are dogshit" to "local models are good actually" (like, a 12 month window from A to B). I don't think they're actually good ENOUGH yet. We need an Opus 4.5 quality local model. When that happens, I think the world will spill over.

Opus 4.5 is/was amazing, and is more than good enough for almost all tasks still as long as you pair with a frontier-level planner/judge. 

It'll still require a hugely expensive machine to run it, I'm sure, like a $5K or more laptop or mac studio. But, that's going to be pennies compared to the API costs plus all the benefits of guaranteed privacy and so on.

## 2026-06-18 (https://x.com/mitchellh/status/2067684200522842234)

I have a genuine question about the NetJets accident for pilots who follow me. First, I'm deeply sorry to those who lost someone in this accident. Second, I'm not passing any judgement on the pilots. I just have a genuine question here trying to learn more:

Why did they do an emergency descent south of the field to line up for a typical straight-in versus doing a flameout descent and approach over the field?

I watched the Blancolirio analysis and he brought it up too, but noted that its a "military maneuver" and that airline guys (and implied NJ) don't do this. Why/why not? (Again, I'm genuinely curious)

In my Vision Jet training, I was taught (and retaught in recurrent) to do the flameout maneuver over the field in the case of an emergency descent even if you still have engine power, because it gives you a predictable and measured way to judge your descent and feel very confident you'll make the field. For the VJ, that is an alt divisible by 3000 over high key and 1500 over low key. So as long as you get into an altitude divisible by 3000 over high key, you SHOULD (pilot skill pending) always reach the field. Repeat loops as necessary.

Full disclaimer: I'm a total amateur. I know many NetJets pilots and their operation and they're real pros. They're 1000x better and more experienced than me. Obviously.

I just really want to know more about whether or not this is standard procedure generally, and why or why not.

## 2026-06-19 (https://x.com/mitchellh/status/2067970516951150721)

Got em. I poison my AGENTS.md (and other things like code comments) all over the place with prompt injections like this to find people who don't review their code and sling it off to another human. Catches folks all the time and then its an instant ban. 

As I've said, I don't care if you don't review your own code. But if you're submitting code to an OSS project and crossing a human boundary, it is simple courtesy to do some human review.

## 2026-06-22 (https://x.com/mitchellh/status/2069045728475763015)

Do you have a legitimate report or are you just rage baiting on social? We take any leak reports seriously but of course need a reproduction or footprint report or some other method to track it down. 

We run all our tests under Valgrind including various graphics e2e tests and there are no known leaks. That doesn’t mean there aren’t any, just showing we take it seriously and will cover scenarios with tests if we can. 

Let me know, happy to look into this.

If you’re just trying to get internet points though for no reason, okay.

## 2026-06-29 (https://x.com/mitchellh/status/2071657456854605869)

Split layout framework update. Since the last video: focus views animate, corner drags can move both axes, cross-window drag and drop with animation, all animations backed by CoreAnimation, and full accessibility framework integration (e.g. compat with VoiceOver).

The focus view work was the hardest and most complicated. We allow caller-provided SwiftUI views for the focus style, but have to drop that back to a native AppKit/UIKit hosted view for smooth CoreAnimation integration with our other animations so they move in lock-step with our other stuff.

Lot of work to get that to work, but I think it turned out great. The caller lives in easy SwiftUI land we handle that complexity.

The animation timings and curves need to be tweaked. I think some animations are too long or don't feel right. But thats just parameterization at this point...

## 2026-06-29 (https://x.com/mitchellh/status/2071688415524049208)

Oh yeah, I think I forgot to share zoom/unzoom working too. Other panes find their nearest window edge and animate out that way, with a preference to an edge they're touching (overrides closest distance calculation). This is a fun one.

There is some weird artifacts on this (every frame is NOT perfect) that I'm still trying to diagnose. I haven't been able to figure it out yet. :(

## 2026-06-30 (https://x.com/mitchellh/status/2071970573144748514)

Amongst my friends, Spotify is the lowest quality consumer app we still pay for. It certainly has gotten noticeably better in the last couple years (arguably worse). So, this is not the positive look Ant and Spotify are spinning here.

Bigger picture, this is the problem with a lot of AI reporting. It reports completely meaningless metrics like deploys per day or LoC. Why don’t we start reporting consumer satisfaction reports? Actually end state research results. 

All the no nuance AI people always come out and think that this is anti AI. Again, I think AI is great and Claude is great. But this is bad marketing and makes both look like clowns.

## 2026-06-30 (https://x.com/mitchellh/status/2071971627748020409)

Amongst my friends, Spotify is the lowest quality consumer app we still pay for. It certainly hasnt gotten noticeably better in the last couple years (arguably worse). So, this is not the positive look Ant and Spotify are spinning here.

Bigger picture, this is the problem with a lot of AI reporting. It reports completely meaningless metrics like deploys per day or LoC. Why don’t we start reporting consumer satisfaction reports? Actually end state research results. 

All the no nuance AI people always come out and think that this is anti AI. Again, I think AI is great and Claude is great. But this is bad marketing and makes both look like clowns.

## 2026-06-30 (https://x.com/mitchellh/status/2071978637868642593)

App store reviews are like yelp or google reviews. That's not how you get real consumer reports. I assisted consumer studies for two diff companies (just as a eng observer in the room or behind the one-way glass, studies were run by real statisticians). If they're producing videos of this quality, they can do real studies by a 3rd party that by contract has to publish all results so they can't filter.

## 2026-07-02 (https://x.com/mitchellh/status/2072714512147624299)

Fable: I know the correct way to cut this. But first, let me reach out to 10 top chefs and verify. I’ll record a video with fake bread. Then they’ll send a guide that we’ll confirm matches. (1 hour later). Okay, my original plan I thought of in 5ms was right. *Cut* Bill: $47.55

Also I melted the arctic in the process.

## 2026-07-02 (https://x.com/mitchellh/status/2072715852944957531)

I'm having a lot success using Fable xhigh as a planner/architect, using GPT 5.5 xhigh (subscription) as a coder, then Fable xhigh again as a judge. At API pricing, planning+judge costs are in the ~few dollar range compared to typical $50+ full round trips. 

I've seen some others using dumber/cheaper coders, but GPT 5.5 even at xhigh compared to Fable 5 is very cheap and very fast. And GPT 5.5 is just... really good.

Still been less than 24hrs since the re-release so the longevity of this approach is unclear, but its been working really well.

## 2026-07-06 (https://x.com/mitchellh/status/2074176376178110866)

One of the changes made to improve Ghostty IO throughput was to introduce a new IO gather thread, bringing our total thread count to 3 per terminal instance. Under heavy IO load, this keeps our VT processing working at nearly full bandwidth without stalls. 

Previously, Ghostty's IO thread (since 2023!) followed this general shape:

read_pty(); exit_if_quitting(); process_data()

The problem is that under heavy load, the pty kernel-side buffer becomes full, blocking the writer (e.g. TUI program). So while Ghostty was in `process_data`, the rest of the world just stalled. Then when we got back to `read_pty`, we'd read the next chunk (a syscall), and while we're paying the syscall cost, Ghostty isn't processing VT data.

Additionally, on macOS and Linux, the kernel only gives a max of 1024 bytes out of a `read()` on a pty (even if the buffer on either side is larger). So, when you `read_pty`, you get 1024 bytes and get back to blocking.

I tried reading from the pty until EAGAIN to fill a buffer but it actually didn't move the needle much cause the major slowdown issue were the stalls on eithe rside.

So the gather thread instead sits in a loop of reading from the pty and filling a set of preallocated buffers. If a read is less than 1024 bytes we assume we're not under any write pressure and dispatch immediately. This preserves latency. 

But when we read a full 1024 byte we assume we are under write pressure and sit in a CPU spin loop (the context switch on a blocking read is higher than the time it takes the writer side to write to the pty). We do this until we get less than 1024 bytes or a timeout of 3 nanoseconds passes or the buffer is full (64KB). Then we dispatch.

As a result, under heavy load, Ghostty is effectively processing data through our VT processor at 100% efficiency so IO is fully bottlenecked there, for now.

This was all discovered in concert with LLM usage, which helped pull direct kernel source (XNU + Linux) to validate assumptions, write minimal harnesses in C to quickly verify, and rubber duck some of my approaches.

## 2026-07-06 (https://x.com/mitchellh/status/2074225453217505494)

Mind boggling to me that I can make a thing faster and there's always people that ask "but why?" What kind of mentality is that? The pursuit of excellence does not need justification. Also, I find in so many cases, we can't know the impact of an improvement until we do it.

For example, one I've talked about before: Ghostty's high IO throughput has enabled terminal program (emulator and TUI) fuzzing at a speed thats incomparably fast to prior solutions. This has resulted in upstream patches to resolve issues in popular projects like btop, tmux, and more. 

Speed enabled that anecdotally example that lifted the tides of adjacent communities that don't rely on Ghostty technology at all. I didn't predict this. 

Make things better because they can be better and let the results naturally play out.

## 2026-07-08 (https://x.com/mitchellh/status/2074862990214787301)

I had early access to 5.6/Sol for ~month. Sol is my default. It is faster, plans/judges just as good as Fable, and I think produces better overall work. I’ll reach for Fable still for highly targeted debug or performance work with clear reward functions. 

A cheeky way I describe Sol vs Fable to my friends is that Sol is a charismatic, efficient, talented coworker you’re jealous of. Fable is a genius recluse that is brilliant at its fixations but doesn’t go out, doesn’t date, and you don’t want to hang out with them much lol.

Fable is undefeated at highly targeted debug/security/performance goals. It’s a sight to behold and I was never able to get Sol to push as hard in this category. I’ll keep using it for this.

Sol is better or comparable at everything else, in my experience. Give it a shot, it’s hard to describe but it’s just more enjoyable to work with. 

(Disclaimer I have no financial ties to either lab, wasn’t paid for any of this.)

## 2026-07-09 (https://x.com/mitchellh/status/2075244791571611753)

I’m glad the Bun rewrite blog post focused mostly on the methodology of the port! It’s a good post! Good work @jarredsumner. 

My favorite part is the little detail about the importance of clean context agents for doing different tasks to avoid biases. I’ve found this is a good reason to not use a single long auto compacting coding session for both build and final verify. 

On the cost, I think $165,000 at API pricing for Fable (didn’t verify) is an incredible deal. There’s absolutely no way an engineer with that salary would’ve been able to achieve the milestones Claude did in 11 days. No way. (Even if you break it down to N engineers paid $165K total in 11 days it doesn’t math out)

This does, however, also reconfirm my own biases which is that Fable in particular is most excellent at hard, focused tasks with clear reward functions. I’ve been tweeting about this recently. 

I would absolutely use Fable for this.
