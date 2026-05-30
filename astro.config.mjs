import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://1hcrypto.com",
  integrations: [
    tailwind({
      config: { applyBaseStyles: false },
    }),
  ],
  i18n: {
    defaultLocale: "zh",
    locales: ["zh", "en"],
    routing: {
      prefixDefaultLocale: true,
    },
  },
  markdown: {
    shikiConfig: {
      theme: "github-dark",
    },
  },
});
