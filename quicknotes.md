# Some quick ideas

- For scores: create sample of "known certain" occupations, calibrate "good scores" to those, given classification tool.
- Threshold cut offs could be based on those benchmark scores
- Base these on combinations of "occupations in this group include" and exact titles.
- Conversely, could create "known uncertain" benchmark group to calibrate "bad scores" - ie known nonexistent occupations, e.g. x-wing pilot, dragon tamer, etc.
- Would need to be done for each model used: e.g. occupationcoder, and classifai - per vectoriser.
- In this framework, overall high relative confidence would mean that the model is more confident about the classification in general, but could still mean that the relative difference between suggestions is small. Would this be the case for e.g. "farmer" and "nurse", vs "astronaut" and "dragon tamer"?
- Ideally would like to have a way to combine absolute and relative confidence into a single score.
- Could do this separately for "confidence" and "ambiguity" scores?
