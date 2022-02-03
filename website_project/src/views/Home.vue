<template>
  <div class="home">
    <h1> Welcome to 5373N_R3V13W5!</h1>
    <h2> For user page, Profiles located temporarily at 'localhost:8000/user/userId' - My profile button is now clickable as a link  </h2>
    <div class="userList">
      <router-link v-for="user in users" :to="{ name: 'UserProfile', params: {userId: user.id} }" :key="user.id">
        {{ user.username }}
      </router-link>
    </div>
  </div>
</template>

<script>
import { users } from "../assets/users";

export default {
  name: 'Home',
  setup() {
    return {
      users
    }
  }
}
</script>

<style lang="scss" scoped>
.home {
  padding: 50px 5%;

  .userList {
    display: flex;
    flex-direction: column;
  }
}
</style>
