# 🚀 First-Time User Quick Checklist

## Pre-Launch Checklist

### Step 1: Get Your API Key ✅
- [ ] Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- [ ] Click "Create API Key"
- [ ] Copy the API key (it's long!)
- [ ] Keep it safe and secret

### Step 2: Prepare Your Computer ✅
- [ ] Python 3.8+ installed ([download here](https://www.python.org/downloads/))
- [ ] Can open command line / terminal
- [ ] Have 500 MB disk space available

### Step 3: Set Up the Project ✅
- [ ] Navigate to project folder
- [ ] Run `run.bat` (Windows) or `bash run.sh` (macOS/Linux)
  - OR manually:
    - [ ] Create virtual environment: `python -m venv venv`
    - [ ] Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
    - [ ] Install: `pip install -r requirements.txt`
    - [ ] Copy `.env.example` to `.env`

### Step 4: Configure API Key ✅
- [ ] Open `.env` file in text editor
- [ ] Replace `your_api_key_here` with your actual API key
- [ ] Save the file
- [ ] ⚠️ **Never share this file or commit it to Git**

### Step 5: Launch the App ✅
- [ ] Run `streamlit run main.py`
- [ ] Wait for "You can now view your Streamlit app" message
- [ ] Browser should open automatically to `http://localhost:8501`
- [ ] If not, click the link in the terminal

---

## First Use Guide

### 🎓 Generating Your First Roadmap

**Step 1: Choose a Topic**
```
Examples:
- "Web Development"
- "Machine Learning"
- "Android Development"
- "Python Programming"
- "Data Science"
- "Cloud Computing"
- "Cybersecurity"
```

**Step 2: Set Your Timeline**
- How much time do you realistically have?
- Honest estimate = better roadmap

**Options:**
- Days: For intensive learning (5 days, 10 days)
- Weeks: Standard courses (4 weeks, 8 weeks)
- Months: Medium projects (3 months, 6 months)
- Years: Mastery programs (1 year, 2 years)

**Step 3: Choose Your Level**
- **Beginner**: Starting from scratch
- **Intermediate**: Have some foundational knowledge
- **Advanced**: Building on expertise

**Step 4: Click "Generate Roadmap"**
- ⏳ Wait 30-60 seconds (AI is thinking!)
- 🎉 Your personalized roadmap appears

### 📖 Understanding Your Roadmap

Your roadmap contains:

**1. Overview** 
- Introduction to the topic
- How to structure your learning
- Why this path is effective

**2. Prerequisites**
- What you should know before starting
- Skills to brush up on

**3. Tools You'll Need**
- Software to install
- Platforms to use
- Free vs paid resources

**4. Learning Modules** (Click tabs to switch)
- **Duration**: Time for each module
- **Objectives**: What you'll learn
- **Key Concepts**: Important ideas
- **Topics**: Subjects to study
- **Resources**: Books, courses, videos

**5. Quizzes** (Click to expand)
- Test your understanding
- Multiple choice questions
- Click "Check Answer" for feedback
- Read explanations to learn more

**6. Projects** (Click to expand)
- Hands-on exercises
- 🟢 Green = Beginner level
- 🟡 Yellow = Intermediate level
- 🔴 Red = Advanced level
- Follow estimated hours

**7. Success Metrics**
- How to know you've mastered it
- Measurable goals

**8. Tips for Success**
- Study strategies
- Motivation tips
- How to stay consistent

### 💾 Saving Your Roadmap

**Option 1: Copy as JSON**
- Click "Copy as JSON"
- Paste into your notes/document

**Option 2: Download**
- Click "Download as JSON"
- File saves to your Downloads folder
- Can open with any text editor

---

## Recommended Learning Topics

Try these topics to explore what the app can do:

### Technology Topics
- [ ] Web Development with React
- [ ] Full Stack Development
- [ ] Mobile App Development
- [ ] Machine Learning with Python
- [ ] Data Science Fundamentals
- [ ] Cloud Computing (AWS/Azure/GCP)
- [ ] DevOps and Docker
- [ ] Cybersecurity Basics

### Skill-Based Topics
- [ ] Time Management
- [ ] Public Speaking
- [ ] Business Writing
- [ ] Project Management
- [ ] Leadership Skills

### Domain Topics
- [ ] Operating Systems
- [ ] Database Design (DBMS)
- [ ] Blockchain Development
- [ ] Game Development
- [ ] IoT Development

---

## Tips for Best Results

### ✅ DO:
- [ ] Be specific with topic names
  - ✅ Good: "Web Development with React"
  - ❌ Bad: "Coding"

- [ ] Be realistic with timeline
  - ✅ Good: "6 months with 5 hours/week"
  - ❌ Bad: "1 month with 1 hour/day"

- [ ] Follow the modules in order
  - Each builds on previous knowledge

- [ ] Complete the quizzes
  - Tests real understanding
  - Don't just guess!

- [ ] Do the projects
  - Real learning happens by doing
  - Build a portfolio

### ❌ DON'T:
- [ ] Don't skip prerequisites
  - They matter!

- [ ] Don't rush through modules
  - Quality > Speed

- [ ] Don't skip hands-on projects
  - Practical experience is key

- [ ] Don't ignore quiz explanations
  - That's where learning happens

- [ ] Don't give up if it's hard
  - Difficulty means you're learning!

---

## Troubleshooting Your First Run

### ❌ Error: "API Key not found"
**Solution:**
1. Open `.env` file
2. Check you pasted the API key correctly
3. No spaces before or after the key
4. Save the file
5. Restart the app

### ❌ Error: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt
```

### ❌ Browser won't open
**Solution:**
- Open browser manually
- Go to `http://localhost:8501`
- If that doesn't work, try `http://127.0.0.1:8501`

### ❌ Generation takes too long (>2 minutes)
**Solution:**
- This is normal, depends on AI response
- Check internet connection
- Try with a simpler topic name

### ❌ Strange characters in output
**Solution:**
- Refresh the page (F5)
- Try generating again
- If persists, try different topic

---

## Getting the Most Out of Your Roadmap

### Weekly Study Routine
1. **Monday**: Read module overview and objectives
2. **Tuesday-Thursday**: Study key concepts and resources
3. **Friday**: Take the quiz
4. **Weekend**: Work on projects

### Tracking Progress
- [ ] Print or save your roadmap
- [ ] Check off completed modules
- [ ] Track quiz scores
- [ ] Share projects with others
- [ ] Celebrate milestones!

### Adapting the Roadmap
- If modules are too easy → move to advanced project
- If modules are too hard → review prerequisites
- If timeline changes → regenerate with new timeline
- If interests shift → generate new roadmap

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+C` | Stop the app |
| `Ctrl+L` | Clear terminal |
| `R` | Rerun app (if needed) |
| `C` | Focus on main area |

---

## Common Questions

**Q: Can I use this offline?**  
A: No, you need internet for AI generation. But you can save/export and review offline.

**Q: How much does this cost?**  
A: Google's free tier gives you plenty. Check [pricing here](https://ai.google.dev/).

**Q: Can I share my roadmap?**  
A: Yes! Download as JSON and share the file with friends.

**Q: Can I use this for courses/groups?**  
A: Absolutely! Generate one per topic and share with students.

**Q: How accurate are the quizzes?**  
A: They're AI-generated. They're good for self-assessment but not official certifications.

**Q: Can I edit the roadmap?**  
A: Downloaded JSON can be edited with text editor, but editing the displayed version happens on page reload.

---

## Next Steps

### After Your First Roadmap:

1. ✅ **Explore**: Generate roadmaps for 2-3 different topics
2. ✅ **Test**: Take a few quizzes to see how they work
3. ✅ **Save**: Download a roadmap you'll actually use
4. ✅ **Plan**: Schedule when to work through modules
5. ✅ **Learn**: Start with week 1 of your roadmap!

### Advanced (After You're Comfortable):

- [ ] Customize the app look (change colors in config.py)
- [ ] Generate roadmaps programmatically (see code examples)
- [ ] Create your own roadmaps collection
- [ ] Integrate with other learning tools

---

## Getting Help

### If Something Goes Wrong:

1. **Check the docs** →  Read SETUP_GUIDE.md
2. **Check the config** → Is .env correct?
3. **Try common fixes** → Reinstall dependencies
4. **Restart everything** → Close app, deactivate venv, restart
5. **Search for similar issues** → Google the error message

### Helpful Resources:

- 📖 **README.md** - What the app does
- 📖 **SETUP_GUIDE.md** - Detailed instructions
- 📖 **PROJECT_SUMMARY.md** - How it all works
- 💬 **Google AI Help** - API support

---

## Success Criteria ✅

Your setup is successful when:

- [ ] App starts without errors
- [ ] You can enter a topic
- [ ] You can generate a roadmap (waits ~30-60s)
- [ ] You can see modules, quizzes, and projects
- [ ] You can take a quiz and get feedback
- [ ] You can download the roadmap

---

## Ready to Start Learning?

**Let's go! 🚀**

1. Pick a topic you're excited about
2. Be honest about your timeline
3. Generate your roadmap
4. Save it
5. Start learning!

Remember: **The best time to start learning was yesterday. The second best time is now.** 📚

---

**Happy Learning! 🎓**

---

*Need help? Check SETUP_GUIDE.md or README.md*
