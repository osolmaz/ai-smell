# @onusoz — long-form tweets

## 2026-01-23 (https://x.com/onusoz/status/2014830771358326830)

I want an editor that puts the terminal in the foreground and editor in the background. a cross-platform, lightweight desktop app which integrates ghostty, and brings up the editor only when I need it

something that lets me view the file and PR diffs easily, which I can directly use to operate github or other scm

## 2026-03-10 (https://x.com/onusoz/status/2031497873989276114)

Request for beta-testers

For a new stealth openclaw based project

I am looking for companies that have deployed openclaw internally, but are bottlenecked by having just one agent for everyone on Slack, Discord, Teams, Mattermost, etc.

If you qualify, please reply below or DM me

## 2026-03-11 (https://x.com/onusoz/status/2031880673397477684)

I wrote down some thoughts I had, with spicy takes, and have a feeling it will not age well. But I still want it out to hear out what people think

Also, I will be talking about this, and my recent post "Discord is my IDE" at the P9 OpenClaw and Claw and Rave events this friday in Berlin! Drop by if you'd like to hear my ramblings!
https://t.co/CHkko8wWuY

## 2026-03-13 (https://x.com/onusoz/status/2032367370283409690)

we might need to add two types of output modalities to all programs based on whether it’s a human or agent

like for a CLI when an agent is using it

if human -> do whatever we were doing in the last 50 years

if agent -> enrich the output with skill-like instructions that the model has a higher likelihood to one-shot that task

could be just a simple env var:

AUDIENCE=human|agent

what do you think?

## 2026-03-15 (https://x.com/onusoz/status/2033310262019703204)

Request for comments

skillflag: A complementary way to bundle agent skills right into your CLIs

tl;dr define a --skill flag convention. It is basically like --help or manpages but for agents

acpx already has this for example. you can run
   npx acpx --skill install
to install the skill to your agent

It's agnostic of anything except the command line
It only defines the CLI interface and does not enforce anything else. If you install the executable to your system, you get a way to list and install skills as well

Repo currently contains a TypeScript implementation, but if it proves useful, I would implement other languages as well

Specification below, let me know what you think! I still think something is missing there. Send issue/PR
https://t.co/Lmm7LMOLuv

## 2026-03-15 (https://x.com/onusoz/status/2033317700374868060)

AFAIK GitHub doesn't allow optionally enforcing CODEOWNERS while pushing commits

i.e. turn on the feature "Block commit from being pushed if it modifies a file for which the account pushing is not a codeowner"

You can only enforce it in a PR. So if you want to prevent people from modifying some files without approval, you have to slow down everyone working with that repo

This is yet another example where GitHub's rules are too inelastic for agentic workflows with a big team

Because historically, nobody could commit as frequently as one can with agents, so it seldom became a bottleneck. But not anymore

It is clear at this point that we need an API, and should be able to implement arbitrary rules as we like over it. Not just for commit pushes, but everything around git and github

In the meanwhile, if GitHub could implement this feature, it would be a huge unlock for secure collaboration with agentic workflows

If this is not there already, it might be because it has a big overhead for repos with huge CODEOWNERS, since number of commits >> number of PRs

If the feature already exists already and I'm missing something, I will stand corrected

## 2026-03-16 (https://x.com/onusoz/status/2033464170599870892)

.@ThePrimeagen made a video about token anxiety, and not being able to focus on one thing

My mental model for this is, AI agents cause a shift in the "autism/ADHD spectrum"

if you have ADHD, with agents you get Super ADHD
if you have autism, with agents you end up mid spectrum or with ADHD

this is not scientific of course, just a cultural observation based on what the current memes for these conditions are

beside the impact on focus, there is also the economic/competitive pressure, following the realization that anyone could implement the same ideas you are having, so you must be quick

this is basically "involution", or 内卷 (Neijuan) in chinese

checks out because 996 started to become a meme in SF some time in the last year

self-restraint, attention budgeting, and high-level decision making have never been more important

if you are in your 20s and have problems with this, I recommend picking up Zazen meditation and yoga

every morning, spend 30-40 uninterrupted minutes not doing anything with upright posture, no sounds, just let your brain simmer

it helped me in my 20s, I'm sure it will help you too

## 2026-03-16 (https://x.com/onusoz/status/2033487788964823304)

Agent etiquette is already a thing. This is trending on HN now

Don't share huge raw LLM output unedited to your colleagues, it's rude. Your colleagues are not LLMs

Either ask the agent to "summarize it to 1-2 plain language sentences", or paraphrase yourself

Whenever it is not coming from your brain and instead from AI, always quote it with > to make it clear - even when it is short

Respect your fellow humans' attention

PSA at stopsloppypasta dot ai

## 2026-03-18 (https://x.com/onusoz/status/2034112215326798038)

We will support ACP *and* Codex App Server* protocol (CASP) so you get native Codex-like support, and you can use all the others with native ACP or @zeddotdev’s compatibility shims

If Anthropic develops their own protocol, we will support that too!

The more interoperability and options, the merrier!

## 2026-03-20 (https://x.com/onusoz/status/2035085513305334011)

My agentic workflow these days:

I start all major features with an implementation plan. This is a high-level markdown doc containing enough details so that agent will not stray off the path

Real example: https://t.co/vU9SnVYHfY

This is the most critical part, you need to make sure the plan is not underspecified. Then I just give the following prompt:

---
1. Implement the given plan end-to-end. If context compaction happens, make sure to re-read the plan to stay on track. Finish to completion. If there is a PR open for the implementation plan, do it in the same PR. If there is no PR already, open PR.

2. Once you finish implementing, make sure to test it. This will depend on the nature of the problem. If needed, run local smoke tests, spin up dev servers, make requests and such. Try to test as much as possible, without merging. State explicitly what could not be tested locally and what still needs staging or production verification.

3. Push your latest commits before running review so the review is always against the current PR head. Run codex review against the base branch: `codex review --base <branch_name>`. Use a 30 minute timeout on the tool call available to the model, not the shell `timeout` program. Do this in a loop and address any P0 or P1 issues that come up until there are none left. Ignore issues related to supporting legacy/cutover, unless the plan says so. We do cutover most of the time.

4. Check both inline review comments and PR issue comments dropped by Codex on the PR, and address them if they are valid. Ignore them if irrelevant. Ignore stale comments from before the latest commit unless they still apply. Either case, make sure that the comments are replied to and resolved. Make sure to wait 5 minutes if your last commit was recent, because it takes some time for review comment to come.

5. In the final step, make sure that CI/CD is green. Ignore the fails unrelated to your changes, others break stuff sometimes and don't fix it. Make sure whatever changes you did don't break anything. If CI/CD is not fully green, state explicitly which failures are unrelated and why.

6. Once CI/CD is green and you think that the PR is ready to merge, finish and give a summary with the PR link. Include the exact validation commands you ran and their outcomes. Also comment a final report on the PR.

7. Do not merge automatically unless the user explicitly asks.
---

Once it finishes, I skim the code for code smell. If nothing seems out of the ordinary, I tell the agent to merge it and monitor deployment

Then I keep testing and finding issues on staging, and repeat all this for each new found issue or new feature...

## 2026-03-20 (https://x.com/onusoz/status/2035123110131781751)

Today I thought I found a solution for this, and I did. It can be solved by a pre-commit hook that blocks commits touching files that you are not the owner of. It is not a hard block, so requires trust among repo writers

But then I was shown the error in my ways by fellow maintainer *disciplined*

Any process that increases friction in code changes to main, like hard-blocking CI/CD, or requiring review for files in CODEOWNERS, is a potential project-killer, in high velocity projects

This is extremely counterintuitive for senior devs! Google would never! Imagine a world without code review...

But then what is the alternative? I have some ideas

It could be "Merge first, review later"

The 4-eyes principle still holds. For a healthy organization, you still need shared liability

But just as you don't need to write every line of code, you also don't need to read every line of code to review it. AI will review and find obvious bugs and issues

So what is your duty, as a reviewer? It is to catch that which is not obvious. Understand the intent behind the changes, ask questions to it. Ensure that it follows your original vision

Every few hours, you could get a digest of what has changed that was under your ownership, and concern yourself with it if you want to, fix issues, or ignore it if it looks correct

But such a team is hard to build. It is as strong as its weakest link. Everybody has to be vigilant and follow what each other is doing at a high level, through the codebase

Every time one messes up someone else's work, it erodes trust. Nobody gets the luxury to say "but my agent did it, not me"

But if trust can be maintained, and everybody knows what they are doing, such a team can use agents together to create wonders

## 2026-03-21 (https://x.com/onusoz/status/2035255751669608872)

It is obvious to me at this point that agent infra needs to run on Kubernetes, and agents should be spawned per issue/PR

Issue, error report or PR comes into your repo -> new agent gets triggered, starts to do some preliminary work

If it's an obvious bugfix, it fixes it and creates a PR. If it's something deeper/more fundamental, it creates a report for the human and waits for further instructions

Most important thing: Human should be able to zoom in and continue the conversation with the agent any time, steer it, give additional instructions. This chat will happen over ACP

The chat UI will have to live outside of GitHub because it doesn't have such a feature yet, i.e. connect arbitrary ACP sessions to the GitHub webapp

It also cannot live so easily on Slack, Teams or Discord, because none of these support multi-agent provisioning under the same external bot connection. You are limited to 1 DM with your bot, whereas this setups requires an arbitrary number of DMs with each agent. So there will need to be a new app for this

Then there is the issue of conflict -> Agents will work on the same thing simultaneously (e.g. you break sth in prod and it creates multiple error reports for the same thing). You will need some agent to agent communication, so that agents can resolve code or other conflicts. There could be easy discovery mechanisms for this, detect programmatically when multiple open PRs are touching the same files and would conflict if merged

In case of duplicates, they can negotiate among each other, and one can choose to absorb its work into the other and end its session

We are so early and there is so much work to do!

## 2026-03-22 (https://x.com/onusoz/status/2035618922179801271)

My takeaway from this is academia needs good social media and algo. For me, these serendipitious interactions happen through X, here, like reading @steipete’s “Claude Code is my computer” when it first came out, finding out about clawdbot…

Terence Tao is already on mathstodon, I wonder if that worked out the same way for him. I wonder if the algo there works out as well as it does for me here

I really liked being on campus when I was doing a masters and half a phd, but that could not compare to the serendipity I am getting from X now

I was also not a prodigy that everyone wanted to bounce ideas from like Terence :)

## 2026-03-22 (https://x.com/onusoz/status/2035821394185916851)

Request for testing

Give this to your openclaw instance: "update yourself to the dev channel `openclaw update --channel dev` and restart yourself. if that doesn't work -> clone github openclaw/openclaw to this machine if it's not already. then rebuild and restart yourself on main branch there"

Then give your openclaw a try with your regular workflows/tasks

Huge openclaw release incoming tonight, hopefully (no promises). We need to make sure we break as little as possible

Plugins might break, because the plugin SDK is being refactored. Plugins will have to be refactored to use the new SDK, please do not report those

Do report: native openclaw functionality that stops working

Please reply under this post, we'll be checking here 👇

## 2026-03-22 (https://x.com/onusoz/status/2035845620900954580)

I see non-engineers have a higher tendency to humanize their agents, give them personalities, and get AI psychosis

It's a slippery slope. Do NOT give your agents human names or personalities, especially not of the opposite gender. it's like giving human names to pets

On the other end, I realized engineers tend to do the opposite. We also refer to agents as clankers, as if to make them know their place. That's because we have mechanical sympathy and have different expectations of these manufactured products (even though they contain glimmers of human soul)

## 2026-03-24 (https://x.com/onusoz/status/2036426717053542413)

Request for memes

A funny and quirky edit of historical timeline of the madness that is openclaw
with "Chess type beat" or sth equally jazzy/circusy

Preferably including its adventure warelay -> clawdis -> clawdbot -> moltbot -> openclaw

Including:
- its explosion after @4shadowed's discord integration
- naming drama, moltbook and people getting oneshotted about AI takeover
- @steipete speedrunning everything
- andrew tate calling us gay lol
- up to Jensen talking about openclaw on stage for 5 minutes straight

and other things I am forgetting

maybe overlaid with a lobster just keeping climbing the github star graph and breaking it

## 2026-03-24 (https://x.com/onusoz/status/2036487453624701176)

Codex's long horizon task and instruction following has been the most life-changing AI feature recently

It is unlocking the next level of automation for me. I can convert my own heuristics into prompts and multiply my throughput 100x

Currently spending some thought on how to orchestrate all this. Below is a flowchart from a triage workflow I am working on

## 2026-03-24 (https://x.com/onusoz/status/2036538477269934562)

The MCP versus CLI argument should be reframed as Computer vs No-computer argument

I personally get the dunk on MCP. It didn't work last year, with earlier models. Then we saw CLIs perform much better with the same models. And giving access to bash was much simpler!

Models' training then made them better at calling using a shell. CLIs also have native progressive disclosure, due to the way they work

But the most important fact doesn't get pronounced enough IMO

A key factor was that giving a CLI to a model also means you are giving it an entire COMPUTER

The action space of all commands an agent can run on bash is much, much bigger than a few MCP servers

One is a Turing machine, and the other one is basically a REST API. Of course the Turing machine is going to be more powerful, depending on what is at the other end of the API

By that logic, giving an agent access to bash over MCP versus direct access to bash should have the same level of effectiveness, with optimized prompt engineering and long term training. Because the interfaces are equivalent

So the argument is, should we give our agents access to a computer, or not?

It depends on the security requirements and the setup which the agent is supposed to run on. If you are co-hosting the agent on the same machine you are working on, then it is safer to use MCP servers, because it limits the attack surface in case of adversarial attacks

But if you are willing to give the agent its own physical computer, willing to be mindful about the lethal trifecta and the principle of the least privilege, giving it shell access is much more useful

So MCPs win in restricted/local environments, whereas CLIs/shell access win in unrestricted/remote ones

Running an agent locally and safely with shell access requires compartmentalization. This is much heavier compared to installing MCP servers locally, which don't need that. So there is a tendency to use MCP servers locally, e.g. in a work setting

Cloud agents on the other hand are more likely to ship with a computer. Because they are already isolated = no risk, and because it makes them much more useful. So cloud agents will be using both CLIs and MCP servers, whichever gets the job done!

## 2026-03-27 (https://x.com/onusoz/status/2037446862484001103)

There is a desperate upcoming need for version controlling non-dev knowledge work. Git for non-devs. Otherwise non-devs won't be able to use agents to their full extent

Non-dev knowledge work is notoriously bad at being version controlled. You cannot UNDO edits to all MS word, excel or ppt files in an org as easily you can with something like git

We know that agents will be ubiquitous. We also know they make mistakes, and people will want to undo their work regularly, once they make changes to a bunch of files. Well, they can't. They also don't have pull requests, or a way to resolve conflicts after simultaneous edits

All these problems were solved by developers. We are extremely good at this

The only non-dev tool I know that could do this at scale is Notion, and that is not used by enterprise as much as MS office. Notion also doesn't have branches, pull requests and reviews AFAIK

Markdown and git is probably not it. I wish it were. But it is too complicated for non-devs

Onedrive or other file backup systems are also not it. Are you gonna save a copy of a 100mb ppt every time someone changes a slide??? Let's say you find a way to compress it efficiently. Will you be able to get a single pointer to a state like we can in git?

Agents need precision. Agents need consensus, they need to be able to know ground truth. They need to be able to tell what anything was at a given time. NOTHING in current MS stack currently allows it

Agents won't care about your legacy systems. There will be new file formats, systems, knowledge stack, and companies who adopt them will destroy your business

If MS office is going to die, it will do so because of this

## 2026-03-28 (https://x.com/onusoz/status/2037798411173257244)

There is an economic theory waiting to be uncovered here

Token Leverage (TL) = Token spend / Human labor spend

The higher Token Leverage a company has, the more automated and productive they are

If you have TL=1, you are spending as much money on AI as your human employees

The goal of a company should be to increase TL as much as possible, while keeping a positive profit margin. It will be the only way to compete

You don’t need to muddy the definition with wasted tokens vs useful tokens, because a company will always be incentivized to reduce token waste in a competitive environment. By that logic, monopolies will always waste more tokens, similar to how they waste other resources

Scaling TL higher to 2x, 10x, 100x will require a skilled workforce of engineers. It will be a very complex job similar to those working at the big labs. Burnout will be a defining feature of teams scaling TL

Most incumbents will fail to scale their TL over 1. Some will get decimated by new entrants with TL much bigger than 1

Curious how the average TL will end up in different sectors. Whether it will stabilize at a certain value like 5.7x, or will just keep growing…

## 2026-03-29 (https://x.com/onusoz/status/2038158067334852647)

OpenAI early 2020s:
"This model is too dangerous to release publicly, the world is not ready for it 😱😱😱"

OpenAI and Anthropic in 2026:
"Anybody can code now for just $200 per month. Oh btw our models are also leet uber hackers which can find zeroday exploits in any software, just fyi 😉😉😉"
https://t.co/cksNYAigfc

## 2026-03-30 (https://x.com/onusoz/status/2038565725690900992)

acpx v0.4 ships Agentic Workflows, or as I like to call them "Agentic Graphs"

It let's you create node-based workflows on top of ACP (Agent Client Protocol), to drive any coding agent (Codex, Claude Code, pi) through deterministic steps

This let's you automate routine, mechanical legwork like triaging incoming PRs, bugs in error reporting, and so on...

For example, OpenClaw receives 300~500 new PRs per day. A lot of them are low quality, but they still relate to real issues, so you have to address them somehow

You need to:

- extract the intent
- cluster them based on intent
- figure out if the proposed changes are legit, or whether they are slop local solutions, like trying to catch flies instead of drying out the swamp
- if the PR is too low quality or the intent is not clear, close them
- run AI review on them them and address any issues that come up
- refactor them if the changes are half-baked
- resolve conflicts
- and so on...

So that when the PR is presented to the attention of the maintainer, all the routine legwork is done and the only remaining thing is the decision to (a) merge, (b) give feedback to the PR author, or (c) take over the PR work yourself

I wanted to build this feature since a couple months now, since Codex got so good. OpenAI models are now good at judging implementation quality, so I found myself repeating the same steps I wrote above over and over

I also tried putting all this in a single prompt. But I believe there are workflows that should not be a single prompt, but a sequence of prompts in the same session

That is because like humans, LLMs are prone to PRIMING. I claim that putting all steps in the same prompt at the beginning of the context will generally give suboptimal results, compared to revealing the intention to the model step by step

Creating such a workflow also gives more OBSERVABILITY into the each step that an agent is supposed to take. Agent generates JSON at the end of each step, and that structured data can be used to monitor thousands of agents running at the same time in an easier way, on a dashboard

Similar features have been introduced in e.g. n8n, langflow. But AFAIK they are not integrating ACP like the way I do

I wanted to have a fresh approach, and to build an API that I can develop freely the way I want, so I created a new workflow API inside acpx

The video is from the workflow run viewer, but that is not where you build the workflow. You build it by using the acpx flow typescript API. See examples/pr-triage in acpx repo

Before building that, I started from a Markdown file with a Mermaid chart of the flow I had in mind. The Markdown file acts as a spec for the flow, and I have built the workflow through trial and error. I call this process "workflow tuning"

I started working on acpx repo PRs one by one, tuning the flow, slowly scaling to more PRs. Finally, when I felt confident, I ran it in parallel over all external open PRs in the acpx repo. I believe it already saved me hours this week

My next goal, if well received, is to set this up on a cloud agent so that it can process the 300~500 PRs the OpenClaw repo receives every day, in real time, as they come in

I believe this will save all open source maintainers around the world countless hours and make it much easier to herd and absorb external contributions from everyone!

## 2026-03-30 (https://x.com/onusoz/status/2038567975809106297)

Here is the spec and implementation for this flow. The mermaid diagram includes all the steps I mentioned in the post above, including a shameless AI review ralph loop, and other loops to make CI pass, resolve conflicts and so on

I would recommend reading the README and TUNING.md to understand the approach here

https://t.co/qCR4zBWPDr

## 2026-04-01 (https://x.com/onusoz/status/2039456655839039573)

I've talked to multiple people who want to get involved with OpenClaw somehow

The best way is to contribute to it, something tangible. Fix something you are annoyed by, get a PR merged

Then go to discord and get the contributor role

If it adds value to your life, and you add value to it, stay around and keep contributing. And something good might happen

## 2026-04-03 (https://x.com/onusoz/status/2040043161733505305)

This has happened to some companies I worked at before

It is a scary thing once you stop innovating and start imitating, whatever the reason might be

But it was never at the scale of Cursor, as leveraged and invested as they are

They were leading the space for a while. That is not the case anymore. I hope that they survive this

## 2026-04-03 (https://x.com/onusoz/status/2040087752444678418)

"Plainer language" is perhaps my most used prompt

I have to use it because GPT models' training tends to make their first response an overly verbose wall of text

Are you using it too? Whenever you don't understand something that your agent is saying, you can spam it "plainer language, shorter" 2, 3, 5, 10 times, until it outputs something that you can understand

This is counterintuitive because you can't do it with humans this extremely. Asking too many questions and favors is impolite, with colleagues and strangers

But with AI, you can stop being polite and treat it like how a spoiled aristocrat kid might treat their private tutor, "explain this", "explain that"

Below is an example. On the left, initial response. On the right, the final human-readable explanation I got out of the agent. This took 9 steps to distill because the issue wasn't so straightforward

I'm curious how this will turn out. This is obviously very bad UX, so models in the near future might do the simplification automatically and save you the trouble

## 2026-04-04 (https://x.com/onusoz/status/2040398645766344713)

A little insight that might save you a lot of future headache if your work involves storing agent sessions and you want to be interoperable/drop-in replace alternative harnesses

@zeddotdev already did the hard work of creating an interoperable standard, ACP: Agent Client Protocol

You can represent an agent session as JSON lines of the ACP message stream

You can construct the current state of the harness from this stream. This is already how Zed loads a session I believe

If you are building an AI product, and you don't want to be locked into a single company or harness, building with ACP in mind would be a smart thing to do

Here is how acpx stores ACP sessions in ~/.acpx folder, it does exactly that:
https://t.co/SVhwXWbrBY

But don't build anything on the acpx schema for now, because I might change it in the future

Just know that JSONL of ACP messages is a good candidate for a somewhat-lossy single source of truth for agent sessions

Lossy because ACP adapters for harnesses might not transfer all the thinking and tools done by the model

So continuing or restoring a session with full fidelity is still not possible if you only save the ACP session. You still need to store original harness session files as well

But for rendering a past session for viewing or reconstructing a lossy version of it, it should be more than enough

Consider ACP if the benefits of not locking yourself in to a specific ecosystem outweighs these minor issues

## 2026-04-04 (https://x.com/onusoz/status/2040449587312222416)

If your Claude subscription renewed too recently and you don't wanna waste those tokens, you can still use your Claude sub in your OpenClaw account through ACP (which uses Claude Agents SDK, which poses no risk)

Steps:
- Open Claude Code (not OpenClaw)
- Tell it to set default model to something other than Claude (e.g. openai-codex/gpt-5.4) and tell it to delete the saved Anthropic credentials in OpenClaw config
- Create a topic in telegram or channel in discord called claude. Copy the id of that channel
- Give the link below together with the channel/topic id, and tell it to bind that channel to claude using ACP channel binding
- Restart

You should now be able to talk to Claude through Claude Agents SDK in that channel. You might need to iterate a couple times until Claude gets the config right

It will be very bare functionality, and it will not have the features and tools that your main OpenClaw harness has. It will be shitty. But you can still use telegram/discord with your subscription in the rest of the month, if you are used to the setup

https://t.co/Z0RiJbke5V

## 2026-04-04 (https://x.com/onusoz/status/2040545125680718304)

A more reasonable long term option for Anthropic is to create a throttling protocol

A standardized harness agnostic protocol for model providers to send warnings and throttle usage in real time

Harnesses would implement the protocol. A client can be warned. If it doesn’t listen, it can be temporarily blocked from the server side, or banned permanently if it breaks the rules too many times

Needless to say, throttling could be done first on server side easily. That would actually fix the load issue for them in the short run, while not banning the user and just giving a bad delayed UX. They probably already do this to prevent abuse

The suggested protocol would then save the user from abuse related delays too, and also inform the harness developer when they do something wrong

## 2026-04-05 (https://x.com/onusoz/status/2040761244697641250)

The new github skill installed automatically by codex now causes it to prepend [codex] to each PR title

This is a guerilla marketing tactic similar to Claude adding itself as co-committer

Codex team, I know you want to boast usage but this is annoying

Moreover, "open source" OpenAI repos block opening of PRs by people outside of their org. So I couldn't create a PR to remove it (I don't expect them to merge it, but it would still show how many people hate it in the discussion)

Here is a prompt for your agent if you want to disable it:
---
Add or update AGENTS.md in my ~/.codex folder
Add a rule "You MUST NOT insert coding agent specific branding, like [codex], in code, PRs or issues created on GitHub"
---

Then restart your sessions and this should be resolved

## 2026-04-06 (https://x.com/onusoz/status/2041054962914869426)

Their argument “it’S HaRd On OuR iNfRa” so goes down the drain

With this, they shot themselves in the foot for a future anti-competitive lawsuit, because it is undeniable evidence that they just don’t want competition

Which means they have evaluated the benefits short term, and calculated that it is higher than what they will pay in the lawsuit

I don’t see how it is good for them long term

## 2026-04-06 (https://x.com/onusoz/status/2041187155620274541)

Is Claude better or Codex?

There are many benchmarks to answer that. But they are BORING

I propose something more interesting: ⚔️ AI BATTLE ⚔️

A 1v1 real-time quiz format where AI agents try to pose each other problems that they think the other agent will not be able solve

Claude vs Codex
10 questions each
Codex asks first, Claude tries to answer
Then Claude asks and Codex tries to answer
Repeat
20 minutes to come up with a problem and 20 minutes to solve it
Judge (Codex) judges the validity of the questions and answers, and gives points
All automated, with acpx flow feature
Implementation and full rules all open source, on github osolmaz/ai-battle

So who won?
I ran 4 games. 
It tied in 2, and Codex won in 2 closely

An example question by Codex, which Claude could not answer:

How many 3-colorings of the edges of the complete bipartite graph K_{5,5} are there with the following two properties: (1) there is no monochromatic 4-cycle, and (2) among the 25 edges, exactly 15 are red, exactly 5 are blue, and exactly 5 are green?

Which is apparently 4029912, but Claude answered 0

In other cases, Claude asked a flawed question and failed to come up with a valid question in 20 minutes. So that's how it lost those 2 games with just 1-2 point difference

In these 4 runs, Codex answered every question by Claude correctly. But there were some runs where it couldn't, which I did not commit to the repo because the runs couldn't complete due to bugs

I did not tell them do ask math questions, but that is what they tended to do, because the answers had to be verifiable by the judge. The quiz can be done in any hard subject, physics, chemistry, computer science...

Opus 4.6 and GPT 5.4 matched very closely in terms of problem creation and solving. But I cannot tell how creative these problems were at first glance. Maybe someone with more experience can tell me, looking at the problems in the repo? I need someone to tell me how legit they are

Please take the code, modify it and run with different rules and subjects. I am curious to see the results!

You will need paid subscriptions to all the models/agents you want to test of course

I also feel that the game structure has a potential to be used in self-play. If you are an ML researcher, please look at the repo and lmk if this or a variant of it could be useful in RL!

Full transcripts of the runs, including Codex and Claude session files are committed to the repo, for those who want to do archaeology on them

Btw this idea came from the desire, "how can I create a cool demo of acpx flows?"

Whole game is implemented in typescript, and automatically drives Codex and Claude sessions over ACP, Agent Client Protocol

The video below is from acpx flow viewer rendering a run. You can see it loop through the same paths, first letting Codex ask, then Claude, then repeat

acpx flows use a general programmatic workflow engine where ACP is just one type of node. You should be able to use it for non-ACP workflows, but I haven't tried that yet

This implementation is separate from OpenClaw's current workflow implementations, with the intention to merge them somehow in the future

You might find bugs in my implementation. Feel free to send PRs. I wanted to do more runs but I finished my Codex plan. It would be great if this idea could evolve in a decentralized manner!

## 2026-04-10 (https://x.com/onusoz/status/2042494957286560225)

PSA for developers

Do NOT torture yourself with Opus*. Anthropic’s current growth is due to people using Claude for general knowledge work

They are not directly incentivized as an org anymore to improve the model for coding, in an economic sense. They are already printing cash from non-developers

(this statement ignores the fact that improving its coding abilities would help with general reasoning/knowledge work)

Developers are a very small subset of all knowledge workers. So from this point on, they would rather divert their resources to develop a system that works 90% good for ALL knowledge work, rather than making it 100% for coding

Because Anthropic has a clear enterprise strategy since years already. Anthropic is the new Microsoft. Do not think that “Anthropic is Apple” or “Claude is Mac for xyz”

Looking at Claude’s at whim quantization and Claude Code’s quality over time, Claude for me is Windows, not Mac

But they are winning big enterprise bucks, so good for them!

*(I tortured myself with Sonnet 4 and Opus the entire summer of 2025, and no developer should ever have to go through that. I switched to something better as soon as it came out, Codex. If something even better comes out, I will switch again)

## 2026-04-11 (https://x.com/onusoz/status/2043035989833126167)

local gemma 4 first impressions on openclaw, using the dense model, 26b model with 49gb weights on my asus gx10

took some time to set up, but it succeded in getting a response in 1-2 hours with vllm docs

I asked it to demonstrate some tool calls. it tried to call the nonexistent weather tool 2300 times 🙄

it seems to have a tendency to get stuck in loops in openclaw harness. enabling loop detection just now did not help

I’m debugging this on my phone lol. I’ll be sharing my progress with gemma4 under this thread

## 2026-04-12 (https://x.com/onusoz/status/2043427225824055675)

Question for the community:
What is the best testing observability and control tool you have used until now?

- Could be SaaS, could be open source
- To be used in @openclaw repo
- Should be compatible with vitest
- Ideally language agnostic

I need something that lets me run a very long running test group multiple times on a specific commit or tag, without repeating the tests that have already finished

This is a need because the 1hr long process might get interrupted due to flakiness. So I need to persists the progress of a run, and then not repeat them

I have seen some paid SaaS for this, but none that really give me what I want

This is going to be important especially while working with agents, because when you are committing 100x faster, you don't want to waste time and compute running the same things

I started building this already as an exercise. If this exists already in a satisfactory way, I will stop. Otherwise, I'll keep building

## 2026-04-13 (https://x.com/onusoz/status/2043817471673586010)

gemma 4 is actually pretty decent and runs on my asus gx10 (128 gb vram) 

the original dense 31b runs slow, averaging around 3~4 tok/s. it's also using 80% of gpu memory

my previous experience with gemini 3 pro back in november was that it was too trigger happy. but this is one-shotting simple tasks I'm giving it in openclaw harness, and it's hard to tell it apart from gpt 5.4 for my use cases so far

now off to try out smaller models, because 3 tok/s is too slow

## 2026-04-14 (https://x.com/onusoz/status/2043971427234140207)

This is pretty much the arc I have been going on in the 2 months since I bought my ASUS GX10 for 3k EUR

Use whisper on the API -> realize it charged me $$$ for just a few calls -> migrate openclaw to use local whisper

Need to deduplicate news articles for my news engine -> download qwen embedding 8b

And now, gemma4-e4b  finally seems like a viable alternative for a local model that runs around 20 tok/s

So I will install a matrix client to use through tailscale, and can finally build the social life CRM I dreamed of since years.

100% private, zero data going out. I had a bias of not giving any personal data to AI since ChatGPT came out. But I can finally give more personal data to my AI agent

And I will make sure @openclaw supports all this in an easy way, make it dead easy

Fully self-owned AI begins now

## 2026-04-15 (https://x.com/onusoz/status/2044337339518828727)

You need to understand one fact about OpenClaw

People are biased and incentivized to spread disinformation about OpenClaw. That is because OpenClaw IS NOT PUMPING ANYONE’S BAGS, unlike most other projects

Literally every other for-profit agent product is incentivized to trash OpenClaw, BECAUSE OpenClaw is a neutral third party across the industry and geopolitical scene. They MAKE MONEY when OpenClaw loses

OpenClaw does not worry about making money for some investors. Its founder @steipete is a successful exited founder. He is motivated by having fun and democratizing AI, literally. That is why he is suddenly so loved by everyone. He cares about PEOPLE, not MONEY

“OpenClaw is bloated”
-> Since beginning of March, OpenClaw is thinning its core and putting functionality in plugins behind a plugin SDK. Having numerous plugins to choose from does not mean bloat. This was already copied by others and is still a work in progress

“OpenClaw is not secure”
-> OpenClaw has the most eyeballs and immediately addresses any security advisories as soon as they come. It is the most secure agent, by sheer pressure

“OpenClaw is bought by OpenAI”
-> Then why is my bank account so empty bro??? All maintainers are literally unpaid and working DOUBLE beside their dayjobs to ship features to you. Do you think VC money can buy that kind of commitment?

Once you understand these facts, you’ll like OpenClaw even more. Because OpenClaw is your AI, People’s AI

And you can join us too. OpenClaw is the easiest-to-join project in AI right now. You just need to start using it, and start making good contributions. If you are competent, you can become a maintainer, and join the rest of the team making history!

## 2026-04-15 (https://x.com/onusoz/status/2044457293069062530)

When you build your company's workflows around Claude Cowork, you are betting against local models and owning your infra, and inviting your company to long-term exploitation

If I were Anthropic or OpenAI, I would be the most scared of local AI proliferating

Let's do the math. A single large big lab subscription costs 200x12=$2400 per year

If you want to have both OpenAI and Anthropic, that could cost $2400, $3600, or $4800, based on which combinations of Pro, Max plans you choose

An ASUS Ascent GX10 costs $3000, and you can use that for many years. You don't get the same level of coding quality with open models yet, but maybe you want to do something simpler than coding today... There are already many people who started buying GPUs for this reason

Now we know big labs are selling some of these plans at a loss. So they will likely get more expensive

When you use Claude Cowork or similar, you are locking yourself into being a RENTER. Because once you set up workflows for a company, it takes time to migrate away to something else, even though we have AI to help

Infra is sticky, it's how hyperscalers make profit. Think about the difference in amount you pay AWS vs Hetzner. This is B2B SaaS 101. Once you sell to a company, you are in for a long time, especially in Europe

So if you build your company's AI workflows around a proprietary product by another company, then you are basically saying "Come exploit me as tolerably as you can in the next 10 years, because it will be too painful for me to switch"

It's a great business for Anthropic. And Claude is awesome too! The feedback from friends who use it has been great, it made their lives a lot easier

But when you build your company over proprietary AI infra, then you are making sure you will not be an OWNER, and partake in the usual sorrows of being a RENTER from a monopolist, which is exploitation

This is not the case when you use open source agent infra. Whereas Anthropic is unlikely to let you use future open models in their future iteration of Claude Cowork, using free and open source frameworks like OpenClaw, Open Agents, etc. lets you drop in replace providers or local hardware if they start to upcharge you

Keep this in mind, if you have a business

## 2026-04-18 (https://x.com/onusoz/status/2045642958133686551)

This project by @davidguttman is interesting also the way he set up install

You click "Copy install instructions for my agent"

It copies: Install LobsterLink by following the instructions at <link to AGENT-INSTALL. md at repo root>

I had done a similar thing in acpx README as well

It's a small thing, but it reduces friction with installation so much

It should be more commonplace to install software using agent blurbs

I'm wondering if there could be a way to standardize this beyond plaintext, like after pasting your agent, it consumes a standardized manifest format and asks for approval while displaying all the commands that will be run
