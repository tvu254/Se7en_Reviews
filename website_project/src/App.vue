<template>
  <div id = "app">
    <UserProfile/>
    </div>
</template>

<script>
import UserProfile from "./components/UserProfile.vue"

export default {
  name: 'App',
  components: { UserProfile }
}
</script>

<style>
#app {
 font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #b9b9b9;
  min-height: 100vh;
  background-color: #0d1424;
}
</style>
