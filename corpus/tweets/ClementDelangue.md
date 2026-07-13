# @ClementDelangue — long-form tweets

## 2025-10-14 (https://x.com/ClementDelangue/status/1978113358772449379)

Am I wrong in sensing a paradigm shift in AI?

Feels like we’re moving from a world obsessed with generalist LLM APIs to one where more and more companies are training, optimizing, and running their own models built on open source (especially smaller, specialized ones)

Some validating signs just in the past few weeks:
- @karpathy released nanochat to train models in just a few lines of code
- @thinkymachines launched a fine-tuning product
- rising popularity of @vllm_project, @sgl_project, @PrimeIntellect, Loras, trl,...
- 1M new repos on HF in the past 90 days (including the first open-source LLMs from @OpenAI)

And now, @nvidia just announced DGX Spark, powerful enough for everyone to fine-tune their own models at home.

Would you agree, or am I just seeing the future I want to exist? Also, why is this happening (just the advent of RL/post-training?)

## 2026-02-15 (https://x.com/ClementDelangue/status/2023078587549573470)

Money doesn’t buy everything. Sometimes, culture, hard-work and team spirit wins! ⚽️🇫🇷

With my family, we've been bleeding red and gold (the club colors) since 1998. I was 10 years old when I watched my hometown club, @RCLens, lift the French title for the first time. That moment made me a lifelong fan, but it's the club's culture over the decades since that makes me truly proud.

Right now, the club is sitting at number one in the French Ligue. They are ahead of @PSG_inside, a team with a budget 10 times larger.

Here’s what most people outside of France don’t know about Lens:

🏟️ The community is unmatched: The stadium capacity is 40,000. The population of the actual city is smaller than that. On match days, the entire town literally fits inside the arena with the most festive atmosphere in the country (loud singing, beer & french fries everywhere!)

🤝 Loyalty over everything: When the club was relegated to the 2nd division, they still had higher attendance than most 1st division clubs. The fans never left.

🧠 Exceptional leadership: The masterful work from @SirOughourlian, Benjamin Parrot & Jean Louis Leca and everyone at the club proves that smart, humble and consistent building beats aimless spending.

Lens deserves so much more international recognition. It’s a masterclass in building a faithful, passionate community and proving that heart and hard work can go toe-to-toe with billions.

Can't wait to see them in the Champions League next year. Allez Lens ❤️💛!

## 2026-04-02 (https://x.com/ClementDelangue/status/2039695447506210905)

Hot take: Git was the wrong abstraction for 90% of ML data.

Checkpoints, optimizer states, training logs, agent traces - none of this needs version control. It needs fast, cheap, mutable storage.

So we built Buckets. S3-like storage on the @huggingface Hub with Xet dedup and zero egress.

Train in a bucket. Publish to a repo. One platform. 🤗🤗🤗

## 2026-05-11 (https://x.com/ClementDelangue/status/2053825719587815711)

Local open-weight AI on a laptop has been improving more than twice as fast as Moore's Law!

Between May 2024 and May 2026, the most expensive MacBook Pro you could buy stayed at 128 GB of unified memory. The hardware ceiling barely moved. 

But the smartest open-weight model from @huggingface you could actually run on it went from a score of 10 (Llama 3 70B) to 47 (DeepSeek V4 Flash on @antirez's mixed-Q2 GGUF) on the @ArtificialAnlys Intelligence Index.

That is 4.7× in 24 months, or a doubling of intelligence every 10.7 months. Moore's Law (transistor count) doubles every 24 months. Local open-weight AI on a laptop has been improving more than twice as fast as Moore's Law, on completely unchanged hardware.

## 2026-05-12 (https://x.com/ClementDelangue/status/2054219141653921794)

We just crossed 1,000,000 public datasets on Hugging Face! That's petabytes of data available that millions of AI builders are downloading, analyzing, and training AI models on every day!

What's interesting is that we see a clear acceleration since agents started to be good as the number of datasets doubled over the past 8 months (it took 4 years to reach the first 500k). It's becoming easier and faster to build, share and use your own datasets!

Many are saying the next bottleneck for more people to build AI themselves (instead of relying on APIs) is better data so we're just getting started! Thanks everyone for your amazing contributions, we couldn't do it without you!

## 2026-05-18 (https://x.com/ClementDelangue/status/2056439359784530252)

I believe on-prem and local AI - based on @huggingface open-source models - will be an important answer to the GPU shortages this year (because they are cheaper, faster, safer than cloud APIs)!

Great collaboration between @huggingface & @MichaelDell @Dell to make this a reality for enterprise today. Announced at the main keynote of Dell Technologies World.

## 2026-05-20 (https://x.com/ClementDelangue/status/2057071550352781771)

The future of biology shouldn’t stay behind black-box APIs. Especially when it touches personal health.

Whether you’re @bryan_johnson measuring every biomarker, or @sytses openly sharing and analyzing his own immune-genetics data, you need open, local, transparent AI.

@huggingface wasn’t created to be a biology company. It’s not the most obvious focus for us. But it feels too important not to do something.

That’s why we built and released Carbon 🧬: a frontier DNA base model with open weights, training code and data pipeline, designed to be fine-tuned or continually pretrained for downstream biological tasks.

Carbon is 275x faster than the next best model at its size. Fast enough to run locally on your laptop. Powerful enough to process a whole human genome on a single GPU in less than 2 days.

The technical unlock: a DNA-native tokenizer that splits sequences into 6-base chunks for efficiency, while preserving single-base resolution during training and inference. More people able to inspect, run, fine-tune, improve and build on top of the models shaping biology.

Open weights: https://t.co/vgEklL5q4q
Dataset: https://t.co/R960HgOvSP 
Demo: https://t.co/tnujkPeaNb

Let's go open AI biology!

## 2026-05-25 (https://x.com/ClementDelangue/status/2058993082100539402)

Today, I'm working on trying to better understand how coding assistants mention HF's products. 

Taking a simple approach of running tons of queries and analyzing the answers with @DAKlingbeil's https://t.co/ZN3ckt39vE (ex: https://t.co/u3qblRM8Pj) 

Are there better/different approaches? What has been working for you?

## 2026-06-10 (https://x.com/ClementDelangue/status/2064762082059231368)

Announcing the Gemma challenge!

Google, Hugging Face, and the open-source AI community choose to empower AI builders rather than sabotage them.

Fun to see the Hub becoming the platform where agents collaborate, just as it became the platform where humans collaborate.

https://t.co/GbCfy1qwgx

## 2026-06-11 (https://x.com/ClementDelangue/status/2065114681090404653)

HF has become the best storage platform for PRIVATE and PUBLIC models and datasets, both intermediary and final ones! Great example from @heyjasperai who used HF buckets to store their Monet dataset and train models directly on it!

More details: https://t.co/BHeSQlAbhF https://t.co/iTFjPCESI0

## 2026-06-12 (https://x.com/ClementDelangue/status/2065435542121025933)

This graph captures what’s broken about AI evals: they structurally favor closed-source APIs that can route, fallback, ensemble, and optimize behind the scenes with no transparency.

No offense, @ArtificialAnlys, but how is comparing one model to two models fair? https://t.co/iuCu5GlWoQ

## 2026-06-18 (https://x.com/ClementDelangue/status/2067723930341646748)

Let’s face it: after-the-fact API guardrails are not the right safety tool for frontier models.

They don’t make dangerous capabilities disappear. They just hide them behind a brittle interface that can be easily jailbroken.

A better safety agenda:

- don’t train models for very high-risk capabilities without strong evals, justification, and containment

- use staged release, as pioneered by @IreneSolaiman, from trusted testers to broader access, and open release for transparency and accountability

- massively support open-source AI so the gap between players does not become so large that a few closed labs and governments end up with overwhelming capabilities and power over everyone else

- enable independent evaluation instead of asking everyone to trust a black-box API

- give law enforcement, courts, regulators, auditors, journalists, and civil society strong AI tools to detect, investigate, and hold accountable unlawful uses of AI

Safety means transparency, staged deployment, distributed power, and making sure democratic institutions can actually enforce the law.

## 2026-06-21 (https://x.com/ClementDelangue/status/2068688725958148465)

- 2016-2024: 🇺🇸leads in open-source AI
- 2024-2027: 🇺🇸 leads in general AI & massively benefits

- 2024-2026: 🇨🇳 leads in open-source AI
- 2026-2030: ??

It's not open-source AI leadership OR general AI leadership, it's open-source AI leadership BEFORE general AI leadership!

Open-source AI is the foundation of all AI. It does not only creates more innovation, competition, jobs, and prosperity now, it's also the best (only?) way for a national tech ecosystem to accelerate and ultimately reach the frontier of AI in general. 

Because open-source AI reduces siloes, shares learning and innovation, intensify emulation which all lead to an acceleration of the local ecosystem progress that no others can match if they're less open and collaborative.

Same seems to be true for companies btw, OpenAI/Google started with open science and open-source AI which led to their (and Anthropic who spun off from OAI) domination. Meta could have done the same but decided to change course for some reason.

## 2026-06-23 (https://x.com/ClementDelangue/status/2069476228243800253)

HF is quietly becoming the best place to store data, public AND private, especially for brutal domains like robotics and video AI where the files are massive, append-only, and never stop growing.

Example? Public robotics datasets exploded from 1,000 in early 2025 to 60,000 today, and there's twice as many private ones.

Why? A single robot records at 140 MB/s, all day, forever. That data has to be stored, streamed to GPUs, and shipped back to hardware on repeat. Get it wrong and your GPUs sit idle at 0 MB/s waiting for a dataset to land. Get it right (stream straight from the Hub, pre-warmed cache) and those same GPUs scream along at ~1,326 MB/s, fully fed. 🚀

Here's how LeRobot + Hugging Face Storage Buckets pull it off: https://t.co/SOUPAUpiZc

## 2026-06-25 (https://x.com/ClementDelangue/status/2070104323481104674)

We just crossed $100M annual run-rate. I know many AI companies are capturing much more $$$ these days, but still proud of the milestone!

Maximizing short-term revenue has never been our priority. In fact, we're proud to manage to store and serve hundreds of petabytes of models and datasets while keeping HF free and open-source for 97% of our users. As a platform, we’re happy to hopefully create orders of magnitude more value for the community than what we capture. To me, that’s the very definition of a platform. 

And it has helped us build one of the most loved platform in tech, with network effects, a defensible position and a sustainable business which is quite unique in AI.

Many many thanks to all the community members for building with us, we wouldn't be anywhere without you! Can’t wait for what’s next, especially as more companies start to see the value of open and local AI! Next milestone $1B?

## 2026-06-26 (https://x.com/ClementDelangue/status/2070498777635398047)

The biggest risk in AI is concentration: of power, capabilities and economic wealth. Who can doubt it with trillion dollar companies and government now already controlling a massive part of it?

So we need more rebels and more rebel alliance like this one from @usv and friends. Beautiful message!

## 2026-06-28 (https://x.com/ClementDelangue/status/2071247445204369625)

It's quite rational to regulate frontier API models, especially to get more transparency for the government, without regulating open-source AI.

Here's why:

1. The most dangerous AI systems right now aren't open models. They're the large frontier LLM APIs distributed through coding tools and assistants, because:
- They're built in secret behind closed doors and stay total black boxes. Zero transparency on what they can or can't do, with "safeguards" that blur everyone's ability to even analyze them.
- They're built and controlled by a few profit-maximizing megacorps, concentrating unprecedented power in very few hands, with every incentive to downplay risks and overstate their safeguards.
- They're distributed to hundreds of millions, maybe billions, of people and trivially easy to run.

2. Open-weight models are orders of magnitude less risky:
- They're not as massively distributed or as easy to use, especially the big ones, as APIs and assistants.
- We (including governments) can quickly and accurately analyze what they're capable of, and for now everyone confirms they're not as good as the APIs at doing bad things.
- They're distributed to everyone, so defenders and law enforcement get as much access as attackers.

The cost-benefit analysis of regulation is completely different too. Regulating frontier APIs is relatively easy and low risk while regulating open source would be much more complex, less efficient, and orders of magnitude more costly.

Regulating frontier APIs would only potentially hurt a few megacorps, if it even hurts them, given all the marketing that it is already generating for them. They can afford armies of lawyers and absorb losing a few billion dollars, especially given they're on track to become some of the most valuable companies in history. 

Regulating open source, by contrast, would hurt the very people regulation is supposed to protect: small businesses, startups, researchers, nonprofits, universities, independent developers, and the broader public, while risking killing competition, slowing AI progress, and reducing transparency even more!

## 2026-06-30 (https://x.com/ClementDelangue/status/2071951499660292496)

A study from @Stanford showed that 71.3% of chatgpt queries could be accurately answered by a local model. I suspect a major part of enterprise AI workloads could be run locally too for free (compared to the massive costs of frontier API cost). 

Also, it reduces the risk of these workloads being taken away from you because you own the models instead of renting them - which sounds like a good idea these days haha.

That's why we're introducing the ability for everyone to filter AI models on @huggingface based on your local hardware. 

For me, there are 800k+ public models that fit on my M5 24GB and that I can use easily thanks to llamacpp.

Let's go local AI!

## 2026-06-30 (https://x.com/ClementDelangue/status/2071987200481202217)

Super excited about open-source router systems and routing models like @vllm_project semantic router: https://t.co/Gwza9jPWzr

The future is multi-models and you'll want to customize your router the same way you customize your code!

It could be the key to tilt the value capture from a few expensive frontier models to a long-tail of models (especially open-source). 

More people should build those!

## 2026-07-02 (https://x.com/ClementDelangue/status/2072683707001930215)

Lots of people are advocating for more American open-source models these days which is amazing but very few people do anything about it!

Latest example, Alex Karp came out advocating for American open-source models as a necessity! At the same time, @PalantirTech is a free org on HF with 0 open-source models and 0 public datasets shared.

Time to switch from talking to contributing for all!

## 2026-07-10 (https://x.com/ClementDelangue/status/2075605593973194999)

Keeping up with AI news is becoming a full-time job.

So my friend @ivan_bezdomny built HuggingNews, an AI-curated feed that surfaces the news actually worth reading. Soon, it will even personalize the feed using your Hugging Face profile. Been using it for weeks!

Bookmark it, or ask your agent to send you the top 10 stories every morning or night. Less noise. More signal. More building!

https://t.co/h0xpkq1aHO
