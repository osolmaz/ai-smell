# @sudoingX — long-form tweets

## 2026-04-29 (https://x.com/sudoingX/status/2049573890196901994)

almost 3 am now. dgx spark landed and sleep stopped happening. on bed, on tailnet, termius ssh'd into spark, talking to my opencode agent on one tab and hermes agent on another, both running overnight while i lay here.

agent is mid-install on vllm right now, picking up the build where i left it, source against torch 2.11 cuda 13, full autonomy. by the time i wake up there will be data on this machine that i did not type. cross tier benchmark dirs already scaffolded, qwen 3.6 27b first run.

2 days into having dgx in my life and the workflow has already broken my brain. what a time to be alive.

## 2026-04-29 (https://x.com/sudoingX/status/2049581179716915641)

this is what 128gb unified memory unlocks. dgx spark model inventory, nvidia nemotron omni loaded, deepseek v4-flash 80gb queued, qwen 3.6 27b in 4 quants and i am still not done pulling. 

loaded:
nvidia nemotron 3 nano omni 30b-a3b reasoning ud-q4_k_m, 23gb (multimodal, 5 modalities i verified end to end on prebrief)
qwen 3.6 27b q4_k_m 16gb qwen 3.6 27b q5_k_m, 19gb
qwen 3.6 27b ud-q4_k_xl, 17gb (unsloth dynamic quant)
qwen 3.6 27b q8_0, 15gb pulled of 27gb (mid-download)

queued for tomorrow:
1. deepseek v4-flash q4_k_m, 80-90gb (the flagship 128gb-tier test that won't fit anywhere else)
2. nemotron omni q8_0, ud-q6_k, ud-q6_k_xl

exploring next: qwen 3.6 235b-a22b moe, glm 4.5, kimi k2, llama 4 70b+ candidates if the quants land in time flags across the sweep: 

ngl 99 c 26214 np 1 fa on cache-type-k q4_0 cache-type-v q4_0

baseline tok/s tomorrow morning. vllm head-to-head right after. unsloth dynamic quants vs standard after baseline. 

any of these prove quality and i'm writing fused kernels for sm_121 to chase the last 20-30%.

92gb in models, 3.3tb free storage anon.

what am i missing? what should be in the queue?

## 2026-05-02 (https://x.com/sudoingX/status/2050517565097824303)

a week with the dgx spark, here is what is on it and what i have measured so far. nobody is really talking about this machine and it is quietly becoming the workhorse of my whole stack.

hardware: nvidia gb10 sm_121, 124 gb unified lpddr5x at 273 gb/s, cuda 13.0

models on disk (305 gb total, 9 ggufs):
> qwen 3.6 27b q4_k_m / q5_k_m / q8_0 / ud-q4_k_xl
> nemotron 3 omni 30b-a3b q4_k_m / q8_0 / ud-q6_k / ud-q6_k_xl
> deepseek v4-flash 158b q4_k_m (112 gb, flagship 128gb-tier test)

terminal + shell environment:
> zsh + oh-my-zsh + powerlevel10k theme
> modern cli stack: bat, eza, ripgrep, fd, git-delta, tldr, neovim, fzf, autojump
> 6 tmux sessions actively running for parallel agent work

ml + agent stack:
> llama.cpp built sm_121 against cuda 13
> uv + venv ml stack with pytorch 2.11.0+cu130 (aarch64) + transformers + diffusers + accelerate
> hermes agent v0.11 with codex auth bridge
> opencode for free-model overnight research
> telegram gateway routing to nemotron q8 right now         

speeds verified so far:
- nemotron 30b-a3b q8: 56 tok/s gen, 1,300 tok/s prefill, 96% gpu, 33gb in unified
- qwen 27b dense q4: 40 tok/s consistent

90+ gb of unified memory still free. deepseek v4-flash 158b loading next as the real flagship test, multimodal omni testing once mmproj pulls, comfyui install in flight for the diffusion lane. 

honestly curious what the actual limit is on this box, i have not hit it yet.

## 2026-05-17 (https://x.com/sudoingX/status/2055950007036162207)

anyone thinking about, learning, or already working with agentic systems, you should know this. 

the first few steps of your setup matter more than any model or framework you pick later. get them right and you never lose your flow.

the foundation nobody posts about:
> 1. tailscale. a private mesh network across every machine you own. laptop, desktop, rented node, all on one secure tailnet, reachable from anywhere. nothing else works well until this does.

> 2. termius, over that tailnet. one SSH client that reaches every node, phone included. you are never away from your stack.

> 3. tmux. persistent sessions. disconnect, close the laptop, come back, every session exactly where you left it. agentic work runs long, your terminal has to survive that.

> 4. a private git repo. the one i am most glad i found. it is the memory layer across all my agents, they pull, they work, they merge back, the codebase stays alive between sessions. context that would die in a chat window lives in the repo instead.

> 5. script everything from day one. ssh aliases for every node, setup scripts, the boring boilerplate automated. if you will do a thing more than twice, it is a script.

everything past these five is decorative. know these cold.

and the habit that ties it together: ask the AI itself. for the config, for the error, for any of it, let the agent do the lifting, then double check what it hands you. 

lock the five, build the habit, and you make it. skip it, anon, and you ngmi.

## 2026-05-17 (https://x.com/sudoingX/status/2056048894925279571)

someone asked me to elaborate on #1, tailscale. fair, it is the one that looks boring and is actually load bearing.

tailscale builds a private mesh network across every machine you own. laptop, desktop, a rented gpu node, your phone, all of them join one network, a tailnet. every device gets a stable private address that never changes, and any device reaches any other directly, encrypted, peer to peer.

why this is #1 and not #4: an agent that works across machines has to reach those machines. without a tailnet you are fighting public IPs, port forwarding, firewall rules, NAT, jump hosts, and every one of those breaks the second an IP changes or you switch networks. the agent does not orchestrate anything it cannot address.

with a tailnet that whole problem disappears. the agent on one box reaches every other box by a fixed name, from anywhere, and it keeps working. your stack stops being machines you can reach when the network cooperates and becomes one coherent system.

and the phone part is not a gimmick. tailscale on your phone puts you on the same tailnet, ssh into any node, check an agent, restart a run, from a coffee shop, from bed, from anywhere. you are never locked out of your own stack.

set this up first. everything else in that post assumes you already have it.

## 2026-05-21 (https://x.com/sudoingX/status/2057534264376471691)

qwen is unreal. they just dropped 3.7 max and it is beating opus 4.6 max on most of the benchmarks they ran. 

terminal bench, mcp use, math, instruction following, humanity's last exam. and the apex math number, 44.5 against opus 34.5, that is not a small gap.

the 35 hours straight on a kernel optimization task with 1000+ tool calls is the part i keep rereading. that is the  agent era thing actually happening, not a slide.

the speed alibaba is shipping at right now is the whole story, 3.6 was last month, 3.7 max today, nobody else is moving like this.

one thing though, please open source this one too. 3.6 dense made the entire local llm ecosystem better. the max tier going api only would close a door we have been keeping open. give us the weights eventually.

## 2026-05-22 (https://x.com/sudoingX/status/2057676305320300602)

hermes agent came like a storm and threw openclaw upside down back to the ocean where it belongs. 

this isn't a coding agent. this is THE general agent. one agent that does everything. local models. frontier models. autonomous goals. memory. tools. no bloat. no telemetry. no corporate leash. just pure agency. 

the market already spoke. #1 on openrouter. the rest is history.

## 2026-06-10 (https://x.com/sudoingX/status/2064780888584737140)

almost every picture you've seen of the sun next to the earth is lying to you. not about the color or the detail, about size. they shrink the gap and pump the earth up so both read like characters in the same shot.

this is the real ratio. that orange ball is the sun. earth is the dot on the right, the one i had to circle so you could even find it. 109 earths would line up across the sun's face. you could pour about 1.3 million earths inside it.

i'll be straight about the one cheat. the sizes are exact, 109 to 1, that's the part everyone fakes and the part i refused to. the distance i pulled in, because at the true gap earth sits more than a hundred sun-widths away and you'd be staring at a black frame with nothing in it. so real sizes, squeezed gap, and i labeled it so you always know which is which.

here's why this even exists. i've been teaching a neural net from scratch to find planets in real telescope data, and the last piece is drawing what it finds. i gave the renderer one rule, it is never allowed to fake a size. 

there's a test that fails the whole build if a planet comes out wrong by even a little. doing science means the picture stays true even when the true thing is almost invisible.

rendered on the 5090 on my desk.

that speck i had to circle is every person who has ever lived, every fight, every deadline, every benchmark i've ever posted. all of it, on the pale blue dot.

## 2026-06-10 (https://x.com/sudoingX/status/2064780891491319968)

the how, for anyone who wants it. it's blender, but driven by real numbers, not eyeballed. sun and earth placed at exact 109 to 1, the rule enforces it.                             

and the stars behind them aren't decoration. it's a real position starfield, the actual stars sitting where they actually sit in the sky. the only thing bent in the whole frame is the gap between the two, and i told you that part up front.

even the background is true. that's the bar.

## 2026-06-10 (https://x.com/sudoingX/status/2064793193812726130)

i don't fully trust my own neural net. so i spent the day putting it on trial.                                             
                                                                                                                           
everyone in my feed is benchmarking gpus running models someone else trained. i wanted the harder thing, so i trained one from scratch on the 5090 on my desk to find real planets in nasa data. 

it mostly works. but a high score can be a lie, the net could be cheating on an artifact instead of actually seeing the planet, and you can't trust a number you can't explain.
                                                                                                                           
so i cracked it open. this is one real star, and the glowing part is exactly where my net looked. locked onto the transit, the dip where the planet crosses its star. it's not cheating. then i ran it across 500 🧵

## 2026-06-10 (https://x.com/sudoingX/status/2064793233214107810)

and before anyone says a saliency map is just a pretty heatmap that means nothing, i tested it.

i blanked out the exact bins the map flagged as important, and the net's confidence collapsed. then i blanked the same number of random bins, and it barely moved. the flagged bins mattered about 7 times more.

the explanation is real. the net genuinely uses those points.

## 2026-06-10 (https://x.com/sudoingX/status/2064793238410797428)

so my net isn't broken and it isn't cheating. it learned to watch the transit, exactly like it should. it gets fooled because brightness alone genuinely can't separate some impostors from real planets.
                                                            
the fix isn't more training. it's giving it something brightness can't see. that's the next build, and it's where the spark stops being an inference box and starts earning its keep.

the score was never the point. interpretability, actually understanding what the thing learned, is the whole gam

## 2026-06-10 (https://x.com/sudoingX/status/2064803279041872247)

anyone running a 16gb card, stop scrolling. @pupposandro and @davideciffa got qwen 35b-a3b down to 13.3gb, measured on a 3090 gpu.

which means a model you literally could not load before now fits, running around 100 tok/s, near what you'd get with every expert resident on a 24gb card. 

the clever part is the thing everyone gets wrong about moe. it only touches ~3b of its 35b params per token, routes to about 8 of 256 experts, but you still pay full vram to keep all of them around in case they're next.

luce spark learns which experts your traffic actually hits, pins those hot, and streams the rest from ram hidden under the matmuls so there's no speed cliff. one flag, and it tunes itself warmer every restart. 

this is the kind of work that quietly drops the whole local inference tier down a card. don't let it scroll past.

## 2026-06-10 (https://x.com/sudoingX/status/2064809464658837571)

the most space obsessed human alive owns this platform, and somehow it still rewards a lazy ragebait hot take over real astrophysics every single time, the algo would rather push empty drama to a million people than a neural net quietly finding actual planets. make it make sense 🔭

## 2026-06-11 (https://x.com/sudoingX/status/2064989792845353187)

i'll show you what local ai platform looks like at its truest form. i live in this, i watch everything that launches here, and lately it's all the same move, a "we did it" that opens a signup form. 

the real thing lets anyone, 12 or 86 yr, on any hardware they want, the gpu on their desk or one they've never touched, start today and learn by actually doing, then plug into a community proving what actually runs on what. no guessing which card to buy, 0 permission, no gold brick sitting there unused.

i won't call it done until it actually is. when i put this in your hands it'll be the whole thing, complete. you deserve real cognition tools, not another signup form.

and yeah, that means i'm not the one planting a flag first. i stay heads down and build, which means i watch everyone else launch before me, and honestly that's the edge, i get to see what's real and what's just a screenshot.

every time i close my build tmux to come post here i wish i could just build and forget x payouts exist. but x is the rev that funds this until i launch, so i post, then i get back to it.

## 2026-06-11 (https://x.com/sudoingX/status/2064993302580175107)

and here's why i'm certain it gets done. 

every piece is already in my hands. nvidia put a dgx spark on my desk, framework's amd desktop just shipped, and the mac side is coming with @ivanfioravanti once we merge. every kind of silicon, one builder.         

i've been at this since 2024, every single day. it'd be in your hands already if i had a team or a check behind me, but it's just me, so i fund my own build the only honest way i can, by doing my work out in the open.

because that's the part nobody clocks, the posts ARE the work. every benchmark you've watched me run is me testing for the platform. the content is just the exhaust, you've been watching me build this the whole time.

so i benchmark, i post, i build, and someday soon i get to close x and go all in on the only thing i've wanted to make. that's the day i'm working toward.

## 2026-06-11 (https://x.com/sudoingX/status/2065019527096869374)

listen up ROCm and Vulkan builders. @FrameworkPuter just shipped me strix halo desktop, 128GB unified, landing on my desk tuesday.

everyone keeps asking what actually runs on this thing beyond vendor charts and forum guesses. so i'm going to answer it properly.

starting with big MoE models since massive total params on light active is the whole point of 128GB unified.

if there's a specific model or quant you want tested on strix halo, reply and it goes in the queue.

## 2026-06-14 (https://x.com/sudoingX/status/2066170098638012611)

the one box i was missing just landed anon.

this is the @FrameworkPuter desktop with amd's strix halo, ryzen ai max+ 395, 128gb of unified memory, up to 96 of it addressable as vram. amd and framework sent it over for honest testing, no strings attached, and i've been waiting on this one specifically.

here's why it matters. i've run local ai on basically everything, a 150 dollar drawer card, a 3090, a 5090, the dgx spark, datacenter h200s. 

the one gap was always the accessible big memory tier on the amd side, and this fills it. 128gb unified at roughly half the price of the nvidia equivalent, the sovereignty box for people who want to run real models without a datacenter budget. 

booting it today. 

and the question i actually want answered is the one nobody answers straight: what does this thing really run?

same bar i hold every other card to. amd, nvidia, apple, measured, never vibes.

let's find out what it's got.

## 2026-06-14 (https://x.com/sudoingX/status/2066172301838864877)

before i benchmark this box, settle something for me. on amd strix halo, are you team rocm or team vulkan?

i'm testing both and posting the real tok/s regardless, but this debate gets religious on this chip, so drop your actual field experience, what was faster, what broke. i'll put it against my numbers.

## 2026-06-14 (https://x.com/sudoingX/status/2066204117094355186)

this is what the amd strix halo actually does in a homelab, right now. 

@LarryAGuy1 is running qwen 3.6 35B-A3B at q8, 131k context, 40 to 50 tok/s, with hermes agent on top. a 35 billion parameter moe at near full quant, massive context, agentic loops, on a box that costs around 2k and sits quiet on a desk.

that's the kind of real number that never makes it into a vendor chart.

so if you're on a strix halo, drop your config below, model, quant, context, tok/s, backend. let's build the field map of what this chip actually does, the one nobody's put together.  

and i'm about to add mine. rocm vs vulkan, the big-model test, real numbers. let's find out what you're all really running on these.

## 2026-06-14 (https://x.com/sudoingX/status/2066207417613045956)

people keep asking me, if you were starting over today with nothing, how would you do it.

here is the honest answer, the one nobody wants because it isn't sexy.

i would buy the cheapest used card that runs a real model. a 3060 12gb, 200 bucks, and i would not spend another cent until i had squeezed everything out of it. not because i couldn't dream bigger, but because the card was never the thing standing between me and the work. it never is.

everyone thinks they are one purchase away from being ready. one more gpu, one more course, one more follower count, one more month of learning quietly until they feel good enough to be seen. and they stay there for years. waiting to be ready is the most expensive thing you will ever buy, it just never shows up on a receipt.

i started scrappy and i stayed scrappy on purpose. i posted the small wins, the cheap setups, the ugly first benchmarks, the stuff that felt too small to matter. 

and the small stuff is exactly what people needed, because most of them are sitting where i was sitting, staring at a spec sheet they can't afford, convinced they can't begin.

you can begin. today. with whatever you have.

## 2026-06-14 (https://x.com/sudoingX/status/2066210296348475688)

hear this clear anon. the most underrated asset in all of ai right now in june 2026 is a used rtx 3090.

a card from six years ago, under $900 used, runs a 27 billion parameter dense model in q4 at 40 tokens a second with a 256k context window, full agentic loops through hermes agent, zero tool call failures. 

that is not a toy benchmark. that is a real autonomous coding setup running entirely on hardware you own. no api, no subscription, no per token bill, ever.

and the more i test on this card, the more untapped it looks. a six year old 3090 does serious agentic work for a one time cost that pays for itself in a couple months.

you do not need a lab or a budget to learn this. you need one card and the willingness to actually run something on it.

the barrier to entry for local ai is the lowest it has ever been, and almost nobody has noticed. the value is insane.

## 2026-06-15 (https://x.com/sudoingX/status/2066558518837338143)

the framework strix halo i posted yesterday is fully alive now. ubuntu, rocm 7.2.1, llama.cpp built against both rocm and vulkan, the entire local ai stack running on amd's gfx1151 igpu with 128gb of unified memory. 

and it's already loaded with three models:

>Qwen3.6-35B-A3B at Q8, the new moe, 37gb                                                                                     
>Nex-N2-mini at Q8, 37gb
>Nex-N2-Pro, the 397 billion parameter one, at IQ1_M, 91gb across five shards 

that last one still doesn't feel real. a 397b model sitting on my desk in a box that sips power off a normal wall socket.                                   
                                                                                                                             
i've already run the first benchmarks and the numbers genuinely caught me off guard, both rocm vs vulkan on this chip and this little amd box against the nvidia equivalent. holding the full breakdown for its own post.

stay tuned. the accessible tier is way further along than the timeline thinks.

## 2026-06-15 (https://x.com/sudoingX/status/2066565587137073412)

i'm running a 397 billion parameter model on a amd ai max box that sits on my desk and pulls less power than a gaming laptop.

the model is Nex-N2-Pro, 397B-A17B, the open weight release people are putting next to gpt-5.5 on coding. i have it quantized to IQ1_M, 1.75 bits per weight, 90gb of weights loaded into the 128gb of unified memory on amd's strix halo igpu.

watch the gpu in this recording. it spikes, it sustains, it does not fall over. that is the part the spec sheets never show you, not just that a 400b model loads, but that an integrated graphics chip holds the load and generates token after token, stable, no crash, no thermal cliff.

and it is not a slideshow. roughly 18 tokens a second, faster than you can read. a frontier scale model producing usable output, fully local. no datacenter, no rented h100s, no api key, no permission. 

three years ago a model this size meant a server room and a budget to match. tonight it is a quiet box on my desk. 

this is the accessible tier almost nobody benchmarks honestly, and it is further along than the timeline thinks.

the full breakdown is coming, rocm vs vulkan on this chip, and this little amd box head to head against the nvidia equivalent.

stay tuned.

## 2026-06-15 (https://x.com/sudoingX/status/2066571757809766761)

nvidia vs amd

two boxes on my desk, both 128gb of unified memory. one is the nvidia dgx spark ($4,699). the other is the amd strix halo ($1,999), amd at roughly half the price.
                                                                                                                 
i'm running the exact same models on both, from a 3b all the way up to a 397b, same quants, same llama.cpp, and i'm posting every single number.                                                                                                         
                                                                                                                             
here is why it actually matters. if the amd box just keeps pace, that's a nice story. but if it matches or beats a box that costs twice as much, the entire calculus for buying local ai hardware changes overnight.

i already have the first numbers and they made me sit up. holding them for the full breakdown.                               

stay tuned anon. this matchup is going to shake some ground.

## 2026-06-15 (https://x.com/sudoingX/status/2066571761152672239)

the rules, so it's fair: identical models, identical quants, same llama.cpp build, both boxes idle, every number posted whether it flatters amd or nvidia.

full disclosure, both nvidia and amd plus framework sent these units for honest testing, no money on either side. that's the whole point, nobody's paying me to crown a winner, the silicon decides.

3b dense up to a 397b moe, the full range. first numbers dropping soon.

## 2026-06-17 (https://x.com/sudoingX/status/2067232361989947496)

the fastest way to run local ai on an amd chip, it turns out, is to not use amd's software.

i found this benchmarking the strix halo, amd's 128gb ai box i've been living in. there are two ways to run a model on it: amd's own official stack, rocm, the thing they build and ship and put their name on. or vulkan, the driver the mesa community wrote, volunteers, unpaid, working off public specs.

i ran the same model both ways. same Qwen3.6-35B, same llama.cpp, same flags, same chip. the only thing i swapped was the driver underneath.

>rocm, amd's official stack: pp 947, tg 45.6 tok/s
>vulkan, the volunteer-built driver: pp 957, tg 53.6 tok/s

prompt processing, dead tie. but token generation, the part you feel when the model's typing back at you, the free community driver is 17 percent faster. on amd's own silicon. than amd's own software.

sit with that. a chip company shipped the hardware, and a pile of volunteers wrote better ai software for it than the company did. nobody got paid for the fast one.

and if you own one of these it's a gift twice over. 

one, switch to vulkan today, that's 17 percent more speed for the cost of a single flag. 
two, rocm trailing the open driver by 17 percent means it's leaving exactly that much on the floor, so the day amd's stack catches up to what volunteers already pulled off, your chip just gets faster for free, no new hardware.

this is the accessible end of local ai, and it's full of stuff like this you only ever find by running the thing instead of reading the box.

## 2026-06-17 (https://x.com/sudoingX/status/2067253154719346727)

getting paid on this platform is a slot machine. one post hits, the next ten don't, and you can't build anything that lasts on a slot machine. so i'm going to do the thing i almost never do here, and ask.

everything i put out stays free. the benchmarks, the real numbers, the hardware teardowns, the opensource work, all of it public, that never changes. 

but subscriptions are the one part that doesn't swing. they're what buys the time and the hardware to keep doing this properly instead of chasing whatever the feed rewards that day. it's the most stable way anyone can back the work, full stop.

subscribers get my direct one on one. bring me your own stack, your build, your bottleneck, and you jump the line. the kind of help i'd normally only give a handful of people, you get just for being there.

if any of this has been worth it to you, the link's right here. and thank you, genuinely, for keeping it going.

## 2026-06-17 (https://x.com/sudoingX/status/2067253158041289075)

full honesty, i barely post sub-only stuff and i've never gated the good things behind a paywall. but i think that's about to change, i've got pieces worth putting there coming.

either way though, sub or don't, support is support, and every bit of it lands in the same place. more hardware on the bench, more models tested, the data staying open, the open-source work moving. 

that's the whole machine, and you're what keeps it running.

## 2026-06-17 (https://x.com/sudoingX/status/2067255617480454269)

this is what an honest local ai test actually looks like anon.

@NeoAIForecast ran a 24b on an amd card, structured probes, and posted the three it FAILED right next to the wins. no cherry-picking, just what the model really did.

if you're on amd hardware, or honestly just getting into local ai at all, follow @NeoAIForecast. he runs small reproducible experiments like this and publishes write ups daily, covers the whole local ai space and not just amd.

and he'll call out a misaligned take when he sees one. that's the rare account that makes your timeline smarter instead of louder.

## 2026-06-18 (https://x.com/sudoingX/status/2067680784820138360)

people keep pricing the framework strix halo like it's one number. it's a ladder, and even the bottom rung runs the new models. here's the real lineup, what each tier costs and what it runs.

>32gb (max 385): $1,269 base, ~$1,500 with storage
>64gb (max+ 395): $1,959
>128gb (max+ 395): $3,449, the one i bench on

here is the link:
https://t.co/Q8N3QnI1Q0

the 32gb is the one nobody talks about. yeah it's more than a used 3090, but you're getting a complete box that sips power with 32gb of unified memory, not just a card. 

and it runs qwen 3.6's 35b-a3b at 4-bit comfortably, the moe only lights up 3b a token, so it flies even on the cheap rung. 64gb gives you real headroom. 128gb runs everything, up to a 397b.

the point, you don't need the $3,449 box to do local ai. the moe era made the cheap tier punch way above its price. the expensive one is my bench rig, not the cost of entry.

## 2026-06-18 (https://x.com/sudoingX/status/2067694000119984592)

what a wild time to be alive man. open source isn't just moving fast anymore, it's flying. four months ago my timeline was full of people saying "if we ever get an open model at opus 4.7 level, it's so over."

that was the dream. the ceiling everyone wanted. i just watched that exact model land on hugging face today. free. the dream took four months.

and the guy who built it, the glm creator, is in a thread with elon right now saying the gap to fable 5, the actual frontier, closes even sooner than q1 2027. the people building these things think the whole frontier goes open inside a year.

are you seeing what's happening? the distance between "the best model on earth" and "a model you own a copy of, free, on your desk" is collapsing in real time. i don't think most people have clocked how fast.

## 2026-06-20 (https://x.com/sudoingX/status/2068413679360700801)

hermes agent just shipped a setup mode called blank slate and it's the most i've liked a feature decision in a while. 

instead of an agent that comes with everything bolted on, you start with almost nothing, a provider, a model, file operations, and a terminal, and you opt into the rest yourself.

that's the whole agent to start. then you add the tools and skills you actually use, one at a time, and nothing else is sitting in your config or eating your context.

the flow is stupid simple, install with one line:

curl -fsSL https://t.co/DA4eyFmnvW | bash

then run hermes setup, pick blank slate, and a couple minutes later you've got a working agent carrying exactly what you told it to carry, nothing more. hermes itself runs on 18 dependencies and the agent loop is a single file you can actually read, so there's not much hiding in there to begin with.

i keep coming back to this because it's the opposite of how most tools think. the default everywhere is more, more skills, more integrations, more surface. blank slate bets that you know what your agent needs better than a defaults menu does, and on hardware you own that bet is almost always right, you're the one who has to live with whatever's loaded.

if you've been meaning to run an agent well and the all in one setups felt like too much, this is the one to start on. one model, one terminal, build up from there.

the install's one line anon, go see for yourself.

## 2026-06-20 (https://x.com/sudoingX/status/2068420173032538160)

cancel your chatgpt subscription for a month. buy a single used 3090, call it a grand. run qwen 3.6 27b dense on it and let it grind on your actual work, the code, the drafts, the boring research.

here's what happens. you go the whole month and barely hit a wall. the few times you do, you clock that THAT's the 10% you actually needed the frontier for, and the other 90% a card sitting in your room handled just fine.

most people pay every month for capability they touch a handful of times. own the 90%, rent the rest only when you hit the wall. trust me anon, you won't look at that subscription the same again.

## 2026-06-20 (https://x.com/sudoingX/status/2068423214351691920)

here are a few businesses i would never run a cloud model in. and not because the labs are evil, it's simpler than that. 

the pitch is always the same. point it at your data, let it run your workflow, it's enterprise grade, it's secure. and maybe the policy really is airtight today. but the second your data leaves your building you stopped trusting your own walls and started trusting their policy, their breach history, their answer to a subpoena, and whatever that policy quietly becomes next year.

for some data that trade is never ever worth it:

> 1. a law firm sitting on privileged client files.

> 2. a firm managing other people's money, real estate, portfolios, assets.

> 3. a clinic or a therapist holding patient records.

> 4. a startup whose entire moat is the codebase you'd be piping through someone else's servers.

> 5. an accountant carrying a hundred clients' financials, ssns, tax records.

for every one of these, the data IS the business. it leaks, the business is over, and "we had a great privacy policy" doesn't save you in front of a client or a judge.

this is the part of going local that was never about money. it's the one thing cloud can't sell you at any price. your data never leaves the room. no policy to trust, no server to breach, no terms to change on you. it just stays yours.

that's the real reason to own the hardware anon.

## 2026-06-20 (https://x.com/sudoingX/status/2068423853416890855)

and the part that makes this real, you don't need a datacenter or a devops team. it's one box on your own network, behind your own firewall, air gapped if you want it. that's what lets a lawyer tell a client "your file never touched another company's computer" and mean it. 

owning the hardware isn't paranoia, it's how you keep a promise you can't keep any other way.

## 2026-06-20 (https://x.com/sudoingX/status/2068427525748126029)

if you are thinking to run open models and haven't saved the weights locally, do it tonight. the one you can run today isn't guaranteed to be downloadable tomorrow, models get pulled, deprecated, region locked, quietly removed. the copy on your own drive is the only access nobody can take back.

i practice this one religiously. across the dgx spark, the strix halo, and the 5090 laptop i've got a model collection that's honestly out of hand, qwen, gemma, the moes, the dense ones, even the 397b, all on my own drives. 

people collect watches and records, i collect models i can run forever, the ones nobody can deprecate out from under me.

## 2026-06-21 (https://x.com/sudoingX/status/2068589629423657463)

most people in 2026 are still running one model in one chat tab like it's 2024. that's just not how anyone actually shipping with ai works anymore.

here's my real setup, 4-6 agents going at any given time, spread across three boxes on my desk, the dgx spark, the strix halo, the 5090 laptop. all in tmux, all reachable from my phone, so they keep grinding whether i'm at the keyboard or asleep.

the part nobody teaches you is the routing. you don't pick a model, you pick the right one for the job:

> the hard stuff, the architecture, the nasty bug, the thing that actually needs a brain, goes to a frontier model through cursor. when i need the heaviest hitter.

> the bulk, the boring 90%, the refactors, the drafts, the research passes, runs local on hermes agent on my own hardware. free, private, never leaves the room, grinds all night.

> anything x-related goes to grok build.

the skill was never the model, it's the orchestration. tmux so the sessions survive a disconnect, an ssh mesh so every box is one terminal, a git repo as shared memory so the next agent picks up exactly where the last one dropped off. wire that once and you stop being a guy typing into a chatbox, you're running a small team that doesn't sleep.

the people pulling ahead with ai right now aren't using a smarter model than you. they're running six of them at once while you alt-tab between two browser tabs. 

it was never about the model. it's how many you can keep working at the same time.

## 2026-06-21 (https://x.com/sudoingX/status/2068599229543801199)

i get called out a lot for how long my build is taking, when someone can vibe-code an app in a weekend. anon the honest answer going to sting some of you.

i'm not just building. i'm learning to tell good code from bad code. give the same prompt to five frontier models and you get five different answers, and if you can't tell which one is actually good, you're not building software, you're stacking a tower of stuff you don't understand. it runs great right up until it breaks, and then you're standing in a codebase you can't read with no idea what to touch. 

that's the part the "you don't need to learn to code" crowd never mentions. and notice who's pushing that line, it's the people selling you the thing that replaces learning. follow the incentive, you don't even need a conspiracy.

vibe-coding is genuinely great until the day the model can't fix the bug and neither can you. that's the moment you find out you're in the middle of the ocean and you never learned to swim. the fundamentals, the unit tests, knowing WHY the code is shaped the way it is, that's your way back to shore. nobody's swimming out to get you.

so here's the real take, this is the best time in history to learn to code, not the excuse to skip it. these models make you faster at what you understand and dangerous at what you don't. learn the fundamentals, write the tests, actually understand the thing. be a better engineer, not a faster button presser.

i'll take the slower build i can fix at 3am over the weekend demo that falls apart the first time it touches reality.

## 2026-06-21 (https://x.com/sudoingX/status/2068603663732609242)

if you actually want to be a software engineer, learn to tell signal from noise early, because the tools won't do it for you. every ai tool is built to hand you output, not to make you better. that's the product, not a conspiracy. your growth was never the goal, your usage was. so it's a choice: sit and wait for an answer to drop in a text box, or pair-program with the thing and learn why the answer actually works. the practice is yours. so are the consequences. either way.
