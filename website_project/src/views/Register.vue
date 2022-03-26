<template>
<form @submit.prevent="handleSubmit">
  <div class="register">
    <h1><strong>Register</strong></h1>

    <div class="formText">
      <label>Username</label>
      <input type="text" class="formBox" v-model="state.username" placeholder="Username"/>
      <br>

      <label>First Name</label>
      <input type="text" class="formBox" v-model="state.firstName" placeholder="First Name"/>
        <br>

      <label>Last Name</label>
      <input type="password" class="formBox" v-model="state.lastName" placeholder="Last Name"/>
      <br>

      <label>Email (only for password recovery)</label>
      <input type="password" class="formBox" v-model="state.email" placeholder="Email"/>
      <br>

      <label>Password</label>
      <input type="password" class="formBox" v-model="state.password" placeholder="Password"/>
      <br>

      <label>Confirm Password</label>
      <input type="password" class="formBox" v-model="state.confirmPassword" placeholder="Confirm Password"/>

    </div>

    <br>
    <div class="invalid" v-if="state.invalid">
      Invalid information entered
    </div>
        
    <div class="badPassword" v-if="state.passwordMismatch">
      Passwords do not match
    </div>
  </div>

   <button class="registerButton">Register</button>

</form>
</template>

<script>
import { reactive } from 'vue';
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  name: 'Register',
  setup() {

    const store = useStore();
    const state = reactive({
      username:  '',
      password:  '',
      confirmPassword: '',
      firstName: '',
      lastName: '',
      email:  '',
      invalid: false,
      passwordMismatch: false
    })
    
      const router = useRouter();
      const handleSubmit = async () => {
        const data = {
        username: state.username,
        password: state.password,
        confirmPassword: state.confirmPassword,
        firstName: state.firstName,
        lastName: state.lastName,
        email:  state.email,
        };
        
        await fetch('http://localhost:5000/register', {
          method: 'POST',
          body: JSON.stringify({ data }),
          headers: {
            'Content-type': 'application/json',
          }
        })
        .then((response) => response.json())
        .then(function (data) {
          console.log(data)
          if (data == "Invalid entry") {
            console.log("invalid entry");
            state.invalid = true
          }
          else if (data == "Invalid password") {
            console.log("invalid username or password");
            state.passwordMismatch = true
          }
          else {
            console.log(data);  
            setUser(data);
          }
        })
        .catch(function (error) {
          console.warn('Something went terribly wrong.', error);

        });
      };

      const setUser = async (user) => {
        await store.dispatch('User/setUser', user);
        console.log(user.Item.username)
        await router.push('/');
      }


    return {
      state,
      handleSubmit,
      store,
      setUser
    }
  }
}
</script>

<style lang="scss" scoped>

.register {
    text-align: center;

    .registerButton {
      text-align: center;
    }
}

</style>
