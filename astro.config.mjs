import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://sentient-autonomics.github.io',
  base: '/conversation-service-landing-page',
  output: 'static',
  build: {
    assets: 'assets'
  }
});