# GitHub Workflows - Status

## ⚠️ No Automated Workflows

This portfolio **does not use GitHub Actions workflows** for deployment.

## ✅ How Deployment Works

The site is deployed **directly from the `gh-pages` branch** using GitHub Pages' built-in static site serving.

### Deployment Process:
1. Static HTML files are stored in the `gh-pages` branch
2. GitHub Pages automatically serves files from `gh-pages`
3. **No build process needed** - site is pre-built and static

### To Update the Site:
```bash
# Switch to gh-pages branch
git checkout gh-pages

# Update the index.html
cp path/to/updated/template.html index.html

# Commit and push
git add index.html
git commit -m "update: site content"
git push origin gh-pages

# Switch back to main
git checkout main
```

## 🚫 Why No Workflows?

- ✅ **Simpler**: No complex build processes
- ✅ **Faster**: No waiting for CI/CD
- ✅ **Reliable**: No workflow failures
- ✅ **Static**: Pure HTML/CSS/JS
- ✅ **Zero Dependencies**: No Python/Node.js needed

## 🌐 Live Site

https://nataliabarros1994.github.io/meu-portfolio-python/

---

**If you see this directory, it means workflows are intentionally disabled.**
