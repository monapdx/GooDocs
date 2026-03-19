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

<img src="https://raw.githubusercontent.com/monapdx/GooDocs/refs/heads/main/img/demo/share-anyone-with-link.gif">

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

Use the provided [PR template](.github/pull_request_template.md) and complete the checklist.

---

Thanks for helping build GooDocs 🚀
