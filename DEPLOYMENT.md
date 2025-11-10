# 🚀 Deployment Guide - Learning Roadmap Generator

## Quick Deployment Options

This guide shows how to deploy your Learning Roadmap Generator to the cloud.

---

## 1. Deploy to Streamlit Cloud (Recommended - FREE!)

### Easiest Option - 5 Minutes

#### Prerequisites:
- GitHub account (https://github.com)
- Streamlit Cloud account (https://streamlit.io/cloud)

#### Steps:

**Step 1: Upload to GitHub**
```bash
# Create a new GitHub repository called "learning-roadmap-generator"
# Clone it locally

# Copy all your files to the cloned folder
# Commit and push:
git add .
git commit -m "Initial commit: Learning Roadmap Generator"
git push origin main
```

**Step 2: Connect to Streamlit Cloud**
1. Visit https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and `main.py` file
5. In "Advanced settings", add your secrets:
   - Key: `GOOGLE_API_KEY`
   - Value: Your API key

**Step 3: Deploy**
- Click "Deploy"
- Wait 2-3 minutes
- Your app is live! 🎉

**Result**: `https://yourname-learning-roadmap.streamlit.app/`

#### Cost: FREE!
Streamlit Cloud offers free hosting for public repositories.

---

## 2. Deploy to Heroku (Legacy - May Have Costs)

### Prerequisites:
- Heroku account (https://www.heroku.com)
- Heroku CLI installed

### Steps:

**Step 1: Create Procfile**
Create file: `Procfile`
```
web: streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
```

**Step 2: Create .streamlit/config.toml**
```toml
[client]
showErrorDetails = true

[server]
port = 8501
headless = true
maxUploadSize = 200
```

**Step 3: Deploy**
```bash
heroku login
heroku create your-app-name
heroku config:set GOOGLE_API_KEY=your_api_key
git push heroku main
```

### Cost: $5-7/month minimum

---

## 3. Deploy to AWS (Advanced)

### Using AWS Elastic Beanstalk

**Cost**: $10-50/month depending on usage

### Steps:
1. Install AWS CLI
2. Create `requirements.txt` (already have this!)
3. Create `ebextensions/.config` for Streamlit
4. Run: `eb create learning-roadmap`
5. Set environment variables in AWS console
6. Deploy: `eb deploy`

### Detailed guide: https://docs.aws.amazon.com/elasticbeanstalk/

---

## 4. Deploy to Google Cloud Run (Simple & Cheap)

### Prerequisites:
- Google Cloud account
- Google Cloud CLI

### Steps:

**Step 1: Create Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
```

**Step 2: Deploy**
```bash
gcloud run deploy learning-roadmap \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars GOOGLE_API_KEY=your_api_key
```

**Cost**: ~$0.25/month for low usage!

---

## 5. Deploy to PythonAnywhere (Beginner Friendly)

### Visit: https://www.pythonanywhere.com

### Steps:
1. Create account
2. Upload your files
3. Create a new web app
4. Select Streamlit
5. Set environment variables
6. Start the app

**Cost**: FREE tier available

---

## 6. Deploy to Replit (Education Friendly)

### Visit: https://replit.com

### Steps:
1. Create account
2. Click "Create Repl"
3. Choose "Python"
4. Upload your files
5. Set secrets (GOOGLE_API_KEY)
6. Click "Run"

**Cost**: FREE!

---

## Deployment Comparison

| Platform | Cost | Ease | Best For | Setup Time |
|----------|------|------|----------|-----------|
| **Streamlit Cloud** | FREE | ⭐⭐⭐⭐⭐ | Public projects | 5 min |
| **Replit** | FREE | ⭐⭐⭐⭐⭐ | Learning/testing | 5 min |
| **PythonAnywhere** | FREE* | ⭐⭐⭐⭐ | Small projects | 10 min |
| **Heroku** | $5-7 | ⭐⭐⭐⭐ | Small apps | 15 min |
| **Google Cloud Run** | $0.25 | ⭐⭐⭐ | Production | 20 min |
| **AWS** | $10+ | ⭐⭐ | Enterprise | 30 min |

---

## RECOMMENDED: Streamlit Cloud

### Why?
1. **FREE** - No charges
2. **Easy** - Just upload GitHub repo
3. **Fast** - Deploy in 5 minutes
4. **Perfect** - Built for Streamlit
5. **Automatic** - Updates when you push to GitHub

### How to Deploy:

**Step 1: Create GitHub Repository**
```bash
# On GitHub.com
# Create new repo: "learning-roadmap-generator"
# Clone it locally
```

**Step 2: Add Your Code**
```bash
# Copy all files to the cloned folder
git add .
git commit -m "Initial commit"
git push origin main
```

**Step 3: Deploy on Streamlit Cloud**
1. Visit https://share.streamlit.io/
2. Sign in with GitHub
3. Select your repository
4. Add secret: GOOGLE_API_KEY=your_key
5. Click "Deploy"

**Done!** 🎉 Your app is live in 3-5 minutes!

---

## Setting Environment Variables

### On Streamlit Cloud:
1. Go to "App settings" (three dots)
2. Click "Secrets"
3. Add your API key:
   ```
   GOOGLE_API_KEY = "your_actual_key_here"
   ```

### On Heroku:
```bash
heroku config:set GOOGLE_API_KEY=your_key
```

### On Google Cloud Run:
```bash
gcloud run deploy ... --set-env-vars GOOGLE_API_KEY=your_key
```

### On AWS:
1. Go to Elastic Beanstalk
2. Select your app
3. Configuration → Software
4. Environment properties → Add:
   - Name: GOOGLE_API_KEY
   - Value: your_key

---

## Monitoring & Logs

### Streamlit Cloud:
- View logs in Streamlit dashboard
- Check "Manage app" section

### Heroku:
```bash
heroku logs --tail
```

### Google Cloud Run:
```bash
gcloud run services describe learning-roadmap --region us-central1
gcloud logging read "resource.type=cloud_run_revision" --limit=50
```

---

## Domain Names

### Add Custom Domain:

**Streamlit Cloud:**
- Upgrade to paid plan
- Add custom domain in settings

**Heroku:**
1. Buy domain (Namecheap, GoDaddy)
2. Go to Heroku app settings
3. Add domain
4. Update DNS records

**Google Cloud Run:**
1. Use Cloud Load Balancer
2. Add SSL certificate
3. Point domain to load balancer

---

## Auto-Updates from GitHub

### Streamlit Cloud:
- Automatically redeploys when you push to GitHub
- No manual action needed!

### Heroku:
1. Go to app settings
2. Enable "Automatic deploys"
3. Select branch (main)
4. Push to GitHub to auto-deploy

### Google Cloud Run:
- Use Cloud Build to auto-deploy on push
- Configure CI/CD pipeline

---

## Security Best Practices

### Before Deploying:
✅ Never commit `.env` file
✅ Use secrets/environment variables
✅ Don't hardcode API keys
✅ Use HTTPS only
✅ Keep dependencies updated

### Environment Variables:
```bash
# Never do this:
GOOGLE_API_KEY = "sk-..." # In code

# Always do this:
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
```

### Keeping Secrets Safe:
1. Keep API keys in environment variables only
2. Use platform-specific secret management
3. Rotate keys periodically
4. Monitor usage for unusual activity

---

## Performance Tips

### Streamlit Cloud:
```toml
# Add to .streamlit/config.toml
[client]
showErrorDetails = true

[server]
maxUploadSize = 200
enableXsrfProtection = true
```

### Optimize Code:
```python
# Cache expensive operations
@st.cache_data
def get_roadmap(topic, timeline):
    return generate_roadmap(topic, timeline)
```

### Reduce Response Time:
- Minimize AI API calls
- Cache results
- Use faster data structures

---

## Troubleshooting Deployment

### App Won't Start?
```bash
# Check requirements.txt
pip install -r requirements.txt

# Check for syntax errors
python -m py_compile main.py

# Check imports
python -c "import streamlit"
```

### Secrets Not Working?
- Check environment variable name matches
- Restart app after setting variables
- Verify platform's secrets syntax

### Slow Performance?
- Check API response time
- Enable caching
- Reduce module reloads
- Optimize data structures

---

## Scaling Your App

### Free Tier Limitations:
- Streamlit Cloud: 1 app
- Replit: 3 projects
- Heroku: 1 dyno (sleeping)

### Scaling Options:
1. **Add more resources**: Pay for better servers
2. **Cache aggressively**: Reduce API calls
3. **Optimize code**: Make it faster
4. **Use CDN**: Speed up assets
5. **Multiple instances**: Load balance

---

## Backup & Recovery

### GitHub as Backup:
```bash
# Your code is always backed up in GitHub
git push origin main  # Always push!
```

### Export Data:
```bash
# Users can export roadmaps as JSON
# Save locally for backup
```

### Recovery:
- If app breaks: Revert to previous commit
- If data lost: Users have JSON exports

---

## Next Steps

1. **Choose a platform** (recommend Streamlit Cloud)
2. **Create account** on chosen platform
3. **Push code to GitHub**
4. **Connect app** to GitHub
5. **Add API key** as secret
6. **Deploy** and test
7. **Share link** with others!

---

## Support

### Platform-Specific Help:
- **Streamlit Cloud**: https://docs.streamlit.io/streamlit-cloud
- **Heroku**: https://devcenter.heroku.com/
- **Google Cloud**: https://cloud.google.com/docs
- **AWS**: https://docs.aws.amazon.com/
- **Replit**: https://docs.replit.com/

### Common Issues:
- Check platform logs
- Verify API key is set
- Ensure requirements.txt is complete
- Test locally first

---

## Sharing Your App

### Once Deployed:

**Share link:**
```
https://yourname-learning-roadmap.streamlit.app/
```

**Embed in website:**
```html
<iframe src="https://yourname-learning-roadmap.streamlit.app/" 
        width="100%" height="600"></iframe>
```

**Social media:**
- Tweet the link
- Post to Reddit
- Share in communities
- Add to portfolio

---

## Analytics

### Track Usage:
- **Streamlit Cloud**: Built-in analytics
- **Google Cloud**: Cloud Monitoring
- **AWS**: CloudWatch
- **Heroku**: Heroku Metrics

### What to Monitor:
- Daily active users
- API usage
- Response times
- Error rates
- Conversion (completion of roadmaps)

---

## Cost Calculator

### Typical Monthly Costs:

| Scenario | Streamlit | Heroku | Google | AWS |
|----------|-----------|--------|--------|-----|
| Low use | FREE | $7 | $0.50 | $20 |
| Medium use | FREE | $50 | $10 | $50 |
| High use | $20 | $250 | $50 | $200 |

For most users: **Streamlit Cloud (FREE)** is perfect!

---

## Final Recommendation

### Start with Streamlit Cloud:
1. ✅ Completely FREE
2. ✅ Takes 5 minutes
3. ✅ No configuration needed
4. ✅ Auto-updates from GitHub
5. ✅ Scalable when needed

### If you need more:
1. **More features?** → Upgrade Streamlit plan
2. **More traffic?** → Move to Google Cloud Run
3. **Enterprise scale?** → Use AWS or Kubernetes

---

**Ready to deploy?** Start with Streamlit Cloud! 🚀

**Questions?** Check the platform's documentation.

**Need help?** See troubleshooting section above.
