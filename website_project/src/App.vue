<template>
  <div id="app">
    <nav>
      <router-link to="/">
        <div class="navigationLogo">
          <img src="./assets/logo.png">
        </div>
      </router-link>
      <router-link to="/browse">
        <div class="browse">
          Browse Reviews
        </div>
      </router-link>

      <div class = "userPost" v-if="user">
        <router-link to="/post">
          <div class="post">
            Post a Review
          </div>
        </router-link>
      </div>

      <div class = "navigationUser" v-if="user">
        <router-link :to="`/user/profile/${user.Item.UserID}`">
          {{ user.Item.UserID }}
        </router-link>
      </div>

      <div class = "loginRegister" v-else>
        <router-link to="/login">
          Login / Register
        </router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
  name: 'App',


  setup() {
    const store = useStore();
    const user = computed(() => store.state.User.user);



    return {
      user,
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #0d1424;
  min-height: 100vh;
  nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 5%;
    background-color: rgba(0, 74, 124, .9);
    color: #d6d6d6;
    .navigationLogo {
      display: flex;
      width: auto;
      height: 40px;
      &:hover {
        filter: brightness(150%);
        transform: scale(1.01, 1.01);
      }
    }
    .navigationUser {
      font-weight: normal;
      font-size: 18px;
      
      &:hover {
        transform: scale(1.025, 1.025);
        filter: brightness(150%);
        .loginRegister {
          font-size: 34px;
        }
      }
    }
    .userPost {
      font-weight: normal;
      font-size: 18px;
      
      &:hover {
        transform: scale(1.025, 1.025);
        filter: brightness(150%);
      }
    }
    .browse {
      font-weight: bold;
      font-size: 18px;
      align-items: center;
      &:hover {
        transform: scale(1.025, 1.025);
        filter: brightness(150%);
      }
    }
    
    .loginRegister {
      font-weight: normal;
      font-size: 18px;
      align-items: center;
      &:hover {
        transform: scale(1.025, 1.025);
        filter: brightness(150%);
      }
    }
  }
}

.button {
  background: rgba(0, 97, 161, 0.9);
  border: 2px solid rgba(0, 97, 161, 0.9);
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.1) 1px 2px 4px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: 16px;
  font-weight: normal;
  line-height: 16px;
  min-height: 30px;
  outline: 0;
  padding: 2px 14px;
  text-align: center;
  text-rendering: geometricprecision;
  text-transform: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
}

.button:hover,
.button:active {
  background-color: initial;
  background-position: 0 0;
  color: rgba(26, 26, 26, 0.9);
}

.button:active {
  opacity: .5;
}
</style>