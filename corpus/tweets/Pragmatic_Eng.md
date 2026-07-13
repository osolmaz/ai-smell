# @Pragmatic_Eng — long-form tweets

## 2026-05-25 (https://x.com/Pragmatic_Eng/status/2058910971897561291)

In Rust, error handling is opt-out, not opt-in. Alice Ryhl (Rust for Android at Google, Rust language advisor & Tokio maintainer) explains:

“The other thing I think is quite good is error handling. So on one hand, Rust doesn't really use exceptions, so it actually returns the error as a value.

So you return a value that's, using an enum, either the result or the error. And the way this is done is that there's an operator `?` - so you write: my_function and then a question mark at the end - which means if this function fails, return the error.

So it's really easy to handle errors but it's not serial characters like it is with exceptions, so it's explicit. On the other hand, if you forget to put the question mark, that's a compilation error.

So you have to check it, and of course you can also have it manually, but the point is it's this idea of there are these things where you write some code and there's some implicit error condition you didn't think of and now you just took down your server or something.”

## 2026-05-26 (https://x.com/Pragmatic_Eng/status/2059265798808445295)

TypeScript was inspired by a strange ask from the outlook team. Anders Hejlsberg(@ahejlsberg)  - creator of C#, TypeScript, Turbo Pascal & Delphi - tells us how TypeScript was born:

“The world started building larger and larger applications in JavaScript. We saw that externally, but also internally.

One of the trigger events was when the outlook team came to see the C# team and asked us whether we would pretty please productize this thing called Script#. 

And we go, well, what is Script#? It's this cross compiler that allows you to cross compile C# into JavaScript such that you can basically treat JavaScript as an instruction language and run your C# apps in a browser.

Why would anyone want to do that?

Well, because then you can get a grownup programming language with grownup tooling. You can use Visual Studio, you can have projects. You can do all of these wonderful things that you can't do with JavaScript because JavaScript is just the scripting language with shitty tooling.

And we thought, well, perhaps a better approach would be to fix JavaScript. I mean, surely you're not going to be best of breed in the JavaScript ecosystem by telling people to write in a different programming language”

## 2026-06-14 (https://x.com/Pragmatic_Eng/status/2066143627932520517)

The dev’s job has always been solving human problems. @kelseyhightower, former Google Distinguished Engineer, on why he’s adopted ‘zero token architecture’ and the importance of thinking for yourself:

“My entire career, I always thought about writing code as decision making.

So before we do anything, we all figure out what needs to happen and then we have to convince the computer to do it. And every key word, every if statement, every function call is a decision we're making. And of course, the syntax kind of gets in the way from time to time. So Stack Overflow, we go.

The importance of thinking for yourself in the age of gen AI:

Then gen AI comes out and in early stages it's kind of like people were just talking to the machine and I've never been impressed by talking to a computer - I'd rather talk to real people. So I don't really care too much about that part. Yes, it mimics human capabilities for people that want to talk to a computer, knock yourselves out.

I'll post things like, ‘hey, I'm adopting the zero token architecture’. People're, like what's zero token architecture? Instead of burning tokens, you learn things and you think for yourself and just complete tasks. And they're like, oh, why would you want to do that?

I was like, we taught the machines. I don't know why people skip this step. ‘Hey Kelsey, there's going to be this artificial intelligence going to do all the things’ like, but we trained it. So all of those times I'm writing code, the books I've published, the comments back and forth on helping people solve problems - it's all in there. Maybe it's arguable that they have their own worldview based on that, and maybe it's slightly different. But I can never put the machine over a person - under any circumstance.

Engineering has always been solving human problems with the best tool for the job:

And I think there's a subset, and I don't want to say everyone in the space is doing this, but there is a healthy subset of people who really believe what is the purpose of a person? Why do we need them to write code? Why do we need them to build software?

It's like maybe you don't understand what the job has always been. We are trying to solve human problems and we use whatever technology is required. In some cases, the technology happens to be software and software ain't required for every human endeavor.”

## 2026-06-15 (https://x.com/Pragmatic_Eng/status/2066517665590427829)

Why Rust doesn't have a garbage collector. Alice Ryhl, Rust for Android at Google & Tokio maintainer, on how memory is freed at the end of scope: 

"I think where Rust is really unique is in the combination of things. So, on one hand, it doesn't have a garbage collector and it's usable in low level contexts like the Linux kernel or firmware or whatever.

[Gergely: "Why is it a good or a bad thing to have a garbage collector? Java has a garbage collector. C# has a garbage collector."]

A garbage collector says once you've done using your objects, there's going to be a little piece of code that checks all of your objects and says, this is not used anymore, and then it cleans it up. 

Whereas, in languages like Rust or C++ the variable is cleaned up at the end of the scope, when it goes out of scope and in the other one they have to detect afterwards. And this little piece of code that runs every so often to check all your objects, for embedded use cases, this might simply not be possible or be unacceptable.

Even for backend it can be a problem because if you have a request incoming it checks all of your objects and you have some sort of latency spike where it takes much longer to reply. So that's one of the reasons it can be helpful in the backend as well."

## 2026-06-30 (https://x.com/Pragmatic_Eng/status/2071942298988916988)

"I have a love-hate relationship with programming". @neetcode1, founder of NeetCode, on getting hooked on coding and why this doesn't always translate to loving a software engineering job:

#1 - Neet loved math and physics, but coding didn’t come naturally

“I was studying electrical engineering when I was in college because I really liked math, I really liked physics. I know a lot of programmers, a lot of programmers don't like math, but they really like programming. And so when I got into programming, I was just taking an intro to C class, it was required for electrical engineering. 

I didn't really want to take it, and I was not very good at it initially. I remember trying to learn `printf` and the `%s`, `%c`. I don't know why I looked around. Everybody around me was learning it so quickly. And to me it was just a very different way of thinking.

Even though it's kind of related to math, you'd think it'd be easy to pick up, but it really wasn't initially for me. 

#2 - Neet got hooked on programming when he realised the problems you can solve with it

Then a couple of months went by and we learned about variables, conditions, loops, functions and all these kind of concepts. 

And then something just kind of clicked where it's like initially programming felt kind of boring. It's like you just have variables and numbers, but then when you introduce all these things, then you realize there's this infinite complexity that can be introduced. And you see that with all the software that is built today where it's like you took these simple primitive things, these zeros and ones, and all of a sudden you just have this enormous universe of software solving insane problems.

Once I really started enjoying programming, I just fell in love with it. And I was like, okay, I'm going to do this for the rest of my life. I'm going to love it. 

#3 - Programming as a job might mean you don’t work on the problems you enjoy

Then I went through a transition where, once I got into the real world, I realized that programming is not something you can just kind of do the way you enjoy. It's a business at the end of the day. So that in a lot of ways took some of the fun out of it for me, where it's like you don't get to work on the languages that you like, the problems that you enjoy solving. You have to focus on the business problems.

I have a love hate relationship with programming because of that reason. And I think a lot of people do.”

## 2026-07-01 (https://x.com/Pragmatic_Eng/status/2072337395215687963)

Replacing a $3,000/month service with a buggy DIY version. @neetcode1, founder of NeetCode, on why it doesn’t make sense to fix it:  

“I have this service that I was paying $3000 a month for. It was for code execution. 
I thought I could write my own version of this within a month or two, but the $3000 a month, the opportunity cost of that versus other things I could be working on, there were other more impactful things that I could be doing. 

But I thought, okay, with vibe coding, maybe I could get this done in less time, maybe a couple of weeks if I'm lucky. I actually got it done in two or three days. It did take coding skills. If I didn't know how to code, I would not have been able to do it, but I got it done in three days, and then I deployed the service. 

Now that I'm managing it, it costs me $200 a month versus $3000. 

But there's a bug in the service. I think there's a memory leak or something. And so what happens is I have this service deployed - every couple days, one or two instances will crash. So there's clearly an issue, there's a production issue. 

I could spend the time to go into that and fix it. This is one of those things where it's like you get into vibe coding and you run into an issue and it's like, okay, now you're going to have to actually dig into the details to really understand where the issue is coming from. So I think it would actually take me much longer than three days to find the issue. 

So I haven't even bothered with that because I'm like, well, okay, if one instance goes down, I'll just have several instances running at the same time. I'll have four. So if one goes down and it doesn't happen that frequently. So it's an interesting trade-off where the engineer in me hates that because there's an issue, fix it. 

But the business value makes no difference. There have been practically zero outages. I have less outages than LeetCode and I'm like a couple people doing it. So I just think it's like a trade-off and people could argue one way or the other, but I think it just makes so much sense right now for me to not fix it.”

## 2026-07-07 (https://x.com/Pragmatic_Eng/status/2074562017222943066)

At Facebook, nobody signed up for @KentBeck's TDD class. Here’s what Kent, who wrote the book on TDD, learnt from the experience: 

“There was a hackathon at Facebook. I thought, I'll give a TDD class because, after all, I wrote the book and they clearly need it. I could see because nobody was doing it, there were very few unit tests at that time, which just shocked me. How can this be?

So I said, I put on the signup sheet, TDD class from me, from ‘the Kent Beck’. Just before my class was one on Argentinian Tango. And just after my class was one on advanced Excel techniques. 

When the time came for the classes, the Argentinian Tango class was full, the advanced Excel class was full, and no one, not one, not even like a pity signup, zero people had signed up for my TDD class. So these engineers clearly felt like they had it already dialed in and they didn't need anything from this old guy.

So I decided, you know what? I'm just going to forget everything that I think I know about software engineering and I'm going to try to do things. I'm just sort of monkey see, monkey do. I'm going to copy what I see people doing and get feedback and see if I can learn to develop in this different style quickly enough. 

Can I relearn software engineering fast enough not to get fired? And I ended up staying there for seven years.”
