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
header, nav, main {
    padding: 1rem;
    width: 100%;
    max-width: 500px;

}

nav, main {
    margin: 0 auto;
    flex: 1;
}

nav {
    display: flex;
    justify-content: space-around;
    margin-bottom: 1rem;
}
</style>
