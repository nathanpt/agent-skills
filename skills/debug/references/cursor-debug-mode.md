[Skip to content](#main)

[Sign in](/dashboard)[ContactContact sales](/contact-sales?source=navbar)[Download](/download)



[Blog](/blog) / [product](/blog/topic/product)

·[product](/blog/topic/product)

# Introducing Debug Mode: Agents with runtime logs

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Falexey-kozy.jpeg&w=48&q=70)

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Falbert-slepak.png&w=48&q=70)

Alexey Kozy & Albert Slepak · 6 min read

Coding agents are great at lots of things, but some bugs consistently stump them. That's why we're introducing Debug Mode, an entirely new agent loop built around runtime information and human verification.

To build it, we examined the practices of the best debuggers on our team. We rolled their workflows into an agent mode, equipping it with tools to instrument code with runtime logs, prompts that generate multiple hypotheses about what's going wrong, and the ability to call back to you to reproduce the issue and verify fixes.

The result is an interactive process that reliably fixes bugs that were previously beyond the reach of even the smartest models working alone, or could take significant developer time to address.

## [#](#describe-the-bug)Describe the bug

To get started, select Debug Mode from the dropdown menu and describe the bug in as much detail as you can.

Instead of immediately trying to generate a fix, the agent reads through your codebase and generates multiple hypotheses about what could be wrong. Some will be ideas you would have thought of on your own, but others will likely be approaches you wouldn't have considered.

The agent then instruments your code with logging statements designed to test these hypotheses. This prepares the agent to receive concrete data about what's actually happening when the bug occurs.

## [#](#reproduce-the-bug)Reproduce the bug

Next, go to your application and reproduce the bug while the agent collects the runtime logs.

The agent can see exactly what's happening in your code when the bug occurs: variable states, execution paths, timing information. With this data, it can pinpoint the root cause and generate a targeted fix. Often that's a precise two or three line modification instead of the hundreds of lines of speculative code you'd have received with a standard agent interaction.

## [#](#verify-the-fix)Verify the fix

At this point, Debug Mode asks you to reproduce the bug one more time with the proposed fix in place. If the bug is gone, you mark it as fixed and the agent removes all the instrumentation, leaving you with a clean, minimal change you can ship.

This human-in-the-loop verification is critical. Sometimes bugs are obvious, but other times they fall into a gray area where the fix might work technically but not feel right. The agent can't make that call on its own. If you don't think the bug is fixed, the agent adds more logging, you reproduce again, and it refines its approach until the problem is actually solved.

This kind of tight back-and-forth is one way we think AI coding works best. The agent handles the tedious work while you make the quick decisions that need human judgment. The result with Debug Mode is that tricky bugs that used to be out of reach are now reliably fixed.

Read the [Debug Mode docs](https://cursor.com/docs/agent/modes#debug). Learn about all the new features in [Cursor 2.2](/changelog/2-2).

## Related posts

[·Product

Bringing the Cursor Agent to Linear

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Frohan-varma-avatar.heif&w=48&q=70)

Rohan Varma · 3 min read](/blog/linear)

[·Product

Closing the code review loop with Bugbot Autofix

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fjon-kaplan.png&w=48&q=70)

Jon Kaplan · 3 min read](/blog/bugbot-autofix)

[·Product

Introducing Plan Mode

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fjai-smith.png&w=48&q=70)

Jai Smith · 2 min read](/blog/plan-mode)

[View more posts →](/blog)

[Skip to content](#main)

[Cursor](/home)

[Sign in](/dashboard)[ContactContact sales](/contact-sales?source=navbar)[Download](/download)



[Blog](/blog) / [product](/blog/topic/product)

·[product](/blog/topic/product)

# Introducing Debug Mode: Agents with runtime logs

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Falexey-kozy.jpeg&w=48&q=70)

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Falbert-slepak.png&w=48&q=70)

Alexey Kozy & Albert Slepak · 6 min read

Coding agents are great at lots of things, but some bugs consistently stump them. That's why we're introducing Debug Mode, an entirely new agent loop built around runtime information and human verification.

To build it, we examined the practices of the best debuggers on our team. We rolled their workflows into an agent mode, equipping it with tools to instrument code with runtime logs, prompts that generate multiple hypotheses about what's going wrong, and the ability to call back to you to reproduce the issue and verify fixes.

The result is an interactive process that reliably fixes bugs that were previously beyond the reach of even the smartest models working alone, or could take significant developer time to address.

## [#](#describe-the-bug)Describe the bug

To get started, select Debug Mode from the dropdown menu and describe the bug in as much detail as you can.

Instead of immediately trying to generate a fix, the agent reads through your codebase and generates multiple hypotheses about what could be wrong. Some will be ideas you would have thought of on your own, but others will likely be approaches you wouldn't have considered.

The agent then instruments your code with logging statements designed to test these hypotheses. This prepares the agent to receive concrete data about what's actually happening when the bug occurs.

## [#](#reproduce-the-bug)Reproduce the bug

Next, go to your application and reproduce the bug while the agent collects the runtime logs.

The agent can see exactly what's happening in your code when the bug occurs: variable states, execution paths, timing information. With this data, it can pinpoint the root cause and generate a targeted fix. Often that's a precise two or three line modification instead of the hundreds of lines of speculative code you'd have received with a standard agent interaction.

## [#](#verify-the-fix)Verify the fix

At this point, Debug Mode asks you to reproduce the bug one more time with the proposed fix in place. If the bug is gone, you mark it as fixed and the agent removes all the instrumentation, leaving you with a clean, minimal change you can ship.

This human-in-the-loop verification is critical. Sometimes bugs are obvious, but other times they fall into a gray area where the fix might work technically but not feel right. The agent can't make that call on its own. If you don't think the bug is fixed, the agent adds more logging, you reproduce again, and it refines its approach until the problem is actually solved.

This kind of tight back-and-forth is one way we think AI coding works best. The agent handles the tedious work while you make the quick decisions that need human judgment. The result with Debug Mode is that tricky bugs that used to be out of reach are now reliably fixed.

Read the [Debug Mode docs](https://cursor.com/docs/agent/modes#debug). Learn about all the new features in [Cursor 2.2](/changelog/2-2).

## Related posts

[·Product

Bringing the Cursor Agent to Linear

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Frohan-varma-avatar.heif&w=48&q=70)

Rohan Varma · 3 min read](/blog/linear)

[·Product

Closing the code review loop with Bugbot Autofix

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fjon-kaplan.png&w=48&q=70)

Jon Kaplan · 3 min read](/blog/bugbot-autofix)

[·Product

Introducing Plan Mode

![](/marketing-static/_next/image?url=https%3A%2F%2Fptht05hbb1ssoooe.public.blob.vercel-storage.com%2Fassets%2Favatars%2Fjai-smith.png&w=48&q=70)

Jai Smith · 2 min read](/blog/plan-mode)

[View more posts →](/blog)