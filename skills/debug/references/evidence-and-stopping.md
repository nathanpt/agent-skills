# Evidence and Stopping Report

## Experiment record

For every diagnostic experiment, record:

```text
Hypothesis:
Prediction:
Experiment:
Observed result:
Conclusion: supported | refuted | inconclusive
Next evidence needed:
```

Do not call an experiment successful merely because the process starts or the test suite is green if the original failure path was not exercised.

## Stopping report

Stop changing application behavior when the evidence is exhausted, contradictory, unsafe to obtain, or still insufficient after three targeted experiments. Report:

```text
Evidence collected:
Hypotheses supported:
Hypotheses refuted:
Current best explanation:
Remaining uncertainty:
Single best next evidence request:
Why further changes would be speculative or unsafe:
```

A precise request for the next log, reproduction, environment detail, or human observation is a valid outcome. Do not convert an unverified hypothesis into a fix merely to end the session.
