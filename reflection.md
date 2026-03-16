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

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
