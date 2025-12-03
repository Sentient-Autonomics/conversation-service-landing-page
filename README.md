# Conversation Service Landing Page

A modern, clean landing page for Conversation Service' AI Conversation Service - an advanced conversation routing system for Indonesian banking with 96% cost reduction compared to traditional LLM solutions.

## 🚀 Features

- **Modern Design**: Clean, professional design with smooth animations and gradient accents
- **Responsive**: Fully responsive layout that works on all devices
- **Performance Optimized**: Built with Astro for blazing-fast performance
- **GitHub Pages Ready**: Pre-configured for easy deployment to GitHub Pages

## 📋 Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Git installed

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/conversation-service-landing.git
cd conversation-service-landing
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Start the development server:
```bash
npm run dev
# or
yarn dev
```

The site will be available at `http://localhost:4321`

## 🏗️ Project Structure

```
/
├── public/             # Static assets
├── src/
│   ├── components/     # Astro components
│   │   ├── Hero.astro
│   │   ├── Stats.astro
│   │   ├── DevelopmentStages.astro
│   │   ├── Features.astro
│   │   ├── CostComparison.astro
│   │   ├── ComplianceSection.astro
│   │   ├── CTASection.astro
│   │   └── Footer.astro
│   ├── layouts/        # Page layouts
│   │   └── Layout.astro
│   └── pages/          # Page files
│       └── index.astro
├── astro.config.mjs    # Astro configuration
├── tailwind.config.mjs # Tailwind CSS configuration
└── package.json
```

## 🎨 Customization

### Logo
To add your company logo:
1. Add your logo file to the `public/` directory
2. Update the logo placeholder in `src/components/Hero.astro` and `src/components/Footer.astro`
3. Replace the SVG placeholder with an `<img>` tag pointing to your logo

Example:
```astro
<img src="/your-logo.png" alt="Conversation Service" class="h-10" />
```

### Colors
The color scheme can be customized in `tailwind.config.mjs`. The main accent colors are:
- Primary Green: `#8BC34A` (accent-lime)
- Secondary Green: `#4CAF50` (accent-green)

### Content
All text content is directly in the component files. Simply edit the relevant `.astro` files to update:
- Company information
- Statistics and metrics
- Feature descriptions
- Pricing information

## 📦 Building for Production

Build the site for production:
```bash
npm run build
# or
yarn build
```

Preview the production build locally:
```bash
npm run preview
# or
yarn preview
```

## 🚀 Deployment to GitHub Pages

### Method 1: Manual Deployment

1. Build the site:
```bash
npm run build
```

2. Deploy to GitHub Pages:
```bash
npx gh-pages -d dist
```

### Method 2: Automatic Deployment with GitHub Actions

1. Update `astro.config.mjs`:
   - Replace `yourusername` with your GitHub username
   - Replace `conversation-service-landing` with your repository name

2. Create a new repository on GitHub

3. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/conversation-service-landing.git
git push -u origin main
```

4. The GitHub Action will automatically build and deploy your site to GitHub Pages

5. Enable GitHub Pages:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: gh-pages
   - Folder: / (root)
   - Click Save

Your site will be available at: `https://yourusername.github.io/conversation-service-landing/`

## 📱 Sections Overview

1. **Hero Section**: Main value proposition with key metrics display
2. **Stats Bar**: Quick overview of cost reduction and performance metrics
3. **Development Stages**: 5-stage R&D process visualization
4. **Features**: Enterprise capabilities highlighting
5. **Cost Comparison**: Detailed comparison table with competitors
6. **Compliance**: Indonesian banking compliance information
7. **CTA**: Call-to-action for demo and whitepaper
8. **Footer**: Site navigation and company information

## 🔧 Technologies Used

- **Astro**: Static site generator for optimal performance
- **Tailwind CSS**: Utility-first CSS framework
- **TypeScript**: Type safety support
- **GitHub Pages**: Free hosting platform

## 📄 License

This project is proprietary to Conversation Service. All rights reserved.

## 📞 Support

For questions or support, please contact:
- Email: support@sentientautonomics.com
- Website: https://sentientautonomics.com

---

Built with ❤️ by Conversation Service
