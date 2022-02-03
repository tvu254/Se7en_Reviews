<template>
  <div id="app">
    <nav>
      <router-link to="/">
        <div class="navigationLogo">
          5373N_R3V13W5
        </div>
      </router-link>
      <router-link to="/user/1">
        <div class = "navigationUser">
          {{ state.user.username }}
        </div>
      </router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { reactive } from 'vue';

export default {
  name: 'App',
  setup() {
    const state = reactive({
      user: {
        username: 'Jakobeus'
      }
    })

    return {
      state
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #a7a7a7;
  min-height: 100vh;
  background-color: #0d1424;

  nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 5%;
    background-color: #a7a7a7;
    color: #0d1424;

    .navigationLogo {
      font-size: 34px;
    }

    .navigationUser {
      font-weight: bold;
      font-size: 20px;
    }
  }
}
</style>