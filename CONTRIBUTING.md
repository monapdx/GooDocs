# Contributing to GooDocs

Thank you for contributing to GooDocs! This project is a curated collection of Google Docs templates, and we welcome high-quality additions.

---

## 🧩 How to Add a Template

### 1. Fork the repository

Click "Fork" and clone your copy locally.

---

### 2. Prepare your Google Doc

- Make sure it is **set to "Anyone with the link can view"**
- Create a **copy link**

Replace:
```
/edit
```

With:
```
/copy
```

---

### 3. Create a preview image

- Take a screenshot of your template
- Save as `.png`
- Recommended size: ~1200px wide

Add it to:
```
img/templates/
```

Example:
```
img/templates/recipe-card.png
```

---

### 4. Add your template to the master list

Open:
```
templates/templates.json
```

Add a new object following the example in:
```
templates/template-entry-example.json
```

⚠️ Make sure:
- JSON syntax is valid (commas, brackets, etc.)
- Your `id` is unique
- Your image path matches your file

---

### 5. Commit and push

```
git add .
git commit -m "Add new template: [Template Name]"
git push
```

---

### 6. Open a Pull Request

Use the provided PR template and complete the checklist.

---

## ✅ Submission Guidelines

Your template should:

- Be useful and reusable
- Be visually clear and readable
- Not contain personal or sensitive information
- Include a working preview image
- Include both view and copy links

---

## 🧠 Tips

Good categories include:
- resume
- newsletter
- planner
- invoice
- notes
- business
- education
- personal
- creative

---

## 🚫 What will be rejected

- Broken Google Doc links
- Missing preview image
- Duplicate templates
- Spam or low-effort submissions

---

Thanks for helping build GooDocs 🚀
