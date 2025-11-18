<script setup lang="ts"></script>

<template>
  <header>
      <h1>DevGrowth</h1>
      <p>Track your daily development progress</p>
  </header>
  <nav>
      <router-link to="/">New Entry</router-link>
      <router-link to="/pastentries">Past Entries</router-link>
  </nav>
  <main>
      <router-view></router-view>
  </main>

</template>

<style scoped>
/* I got help from ChatGPT on styling -Allison */
/* Overall layout containers */
header, nav, main {
    padding: 1rem;
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
    font-family: "Inter", sans-serif;
}

/* Headers */
header {
    text-align: center;
    margin-top: 1.5rem;
}

header h1 {
    font-size: 2rem;
    margin-bottom: 0.25rem;
    color: #1d3b29;
    font-weight: 700;
}

header p {
    color: #4f5d57;
    font-size: 0.95rem;
    margin: 0;
}

/* Navigation Tabs */
nav {
    display: flex;
    justify-content: center;
    gap: 1rem;

    background: #f2f6f3;
    border-radius: 14px;
    padding: 0.5rem 0.75rem;
    margin-top: 1.5rem;
    border: 1px solid #d6e2d8;
}

nav a {
    flex: 1;
    text-align: center;

    padding: 0.5rem 0.75rem;
    border-radius: 8px;
    text-decoration: none;

    font-weight: 500;
    color: #355a3a;

    transition: background 0.2s ease, color 0.2s ease;
}

nav a:hover {
    background: #e3efe5;
}

nav a.router-link-active {
    background: #3e8e57;
    color: white;
    font-weight: 600;
}

/* Main Content */
main {
    margin-top: 1rem;
    padding-bottom: 3rem;
}
</style>
