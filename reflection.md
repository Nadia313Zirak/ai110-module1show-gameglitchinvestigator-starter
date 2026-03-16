# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  
  1ST BUG: What was broken first when I started was the fact that my number was in the range of the 'correct' guess but I would get a message that would say "Go lower" or if I put in a high number it would indicate to go higher. 
  One more bug that I noticed when I tried an edge case, was that the messaeg "Go lower" was desplayed even after I put in a 0 and a negetive number. This was also the case with 'Go higher' but the number is a small number. 

  2ND BUG: Another bug i noticed was the "Attempts left", fo rinstance i woudl have one attempt left but i woudl get a message that would say "out of attempts" 

  3RD BUG: Guess outside allowed range is accepted, the game should only allow guesses between 1 - 100 because the range display "1 to 100" but the game allowed me to enter a guess like 150 which is outside the allowed range, and it still  processed the guess and gave a hint. 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

ANS: I used GitHub Copilot in VS Code and ChatGPT to help identify bugs and understand the code.One correct suggestion from AI was identifying that the hints in the check_guess function were reversed. The AI suggested switching the messages so that a guess higher than the secret returns “Go LOWER” and a lower guess returns “Go HIGHER.” I verified this by running the game with streamlit run app.py and testing different guesses. One misleading suggestion was when the AI suggested comparing guesses as strings. This caused incorrect  because string comparisons do not behave the same as numeric comparisons. I verified this by testing the game and seeing incorrect hints, and then fixed it by keeping both values as integers.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
ANS: To verify that the bugs were fixed, I tested the game manually by running `streamlit run app.py` and trying guesses that were higher, lower, and equal to the secret number. This confirmed that the hints now display the correct direction.I also created automated tests in `tests/test_game_logic.py` and ran them using `pytest`. The tests check that the `check_guess` function correctly returns "Too High", "Too Low", and "Win". All tests passed, confirming that the logic works correctly.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

-ANS:  The secret number kept changing because Streamlit reruns the whole script whenever the user interacts with the app. Since the number was generated in the code, it would reset on each rerun. Streamlit reruns mean the script starts from the top every time something changes in the UI. Session state allows values to persist between these reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?

- ANS: One habit I want to reuse is testing fixes with pytest to make sure the logic works correctly.Next time I work with AI, I would test its suggestions more quickly since some can be incorrect.This project showed me that AI can help explain and suggest solutions, but the developer still needs to test and verify the code.
