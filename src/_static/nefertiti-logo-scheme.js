// A small patch to allow the logo color to switch appropriately in the
// sphinx-nefertiti theme. The theme does not expose separate logo paths for
// light and dark color schemes.

function updateNefertitiLogo() {
  const logo = document.querySelector("img.project-logo");
  if (!logo) return;

  const currentLogo = new URL(logo.getAttribute("src"), document.baseURI);
  const staticDir = new URL(".", currentLogo);
  const lightLogo = new URL("touchbook-logo.svg", staticDir).href;
  const darkLogo = new URL("touchbook-logo-dark.svg", staticDir).href;

  const storedScheme = localStorage.getItem("snftt-color-scheme") || "default";
  const isDark = storedScheme === "dark"
    || (
      storedScheme === "default"
      && document.documentElement.classList.contains("dark")
    );
  logo.src = isDark ? darkLogo : lightLogo;
}

document.addEventListener("DOMContentLoaded", () => {
  updateNefertitiLogo();

  for (const item of document.querySelectorAll("[data-snftt-luz]")) {
    item.addEventListener("click", () => {
      window.setTimeout(updateNefertitiLogo, 0);
    });
  }

  for (const scheme of ["dark", "light"]) {
    window.matchMedia(`(prefers-color-scheme: ${scheme})`)
      .addEventListener("change", updateNefertitiLogo);
  }
});

