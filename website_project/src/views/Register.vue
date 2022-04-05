<template>
<form @submit.prevent="handleSubmit">
  <div class="register">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>
    <div class="formText">
      <label for="first-name">First Name</label>
      <input type="text" v-model="state.firstName" placeholder="Enter First Name"
             name="first-name" id="first-name"/>
      <label for="last-name">Last Name</label>
      <input type="text" v-model="state.lastName" placeholder="Enter Last Name"
             name="last-name" id="last-name"/>
      <label for="user-name">Username</label>
      <input type="text" v-model="state.username" placeholder="Enter Username"
             name="user-name" id="user-name" required/>
      <label for="email">Email</label>
      <input type="text" v-model="state.email" placeholder="Enter Email"
             name="email" id="email"/>
      <label for="psw">Password</label>
      <input type="password" v-model="state.password" placeholder="Enter Password"
             name="psw" id="psw"/>
      <label for="psw-repeat">Confirm Password</label>
      <input type="password" v-model="state.confirmPassword" placeholder="Repeat Password"
             name="psw-repeat" id="psw-repeat" required/>

        <div v-show="state.invalid ">
          <div class="invalid">Invalid data entered</div>
        </div>
        <div v-show="state.usernameTaken">
          <div class="invalid">Username is already taken</div>
        </div>
        <div v-show="state.passwordMismatch">
          <div class="invalid">Passwords do not match</div>
        </div>

    </div>
    <hr>
    <p>By creating an account you agree to our
      <router-link to="/">
        <a href="#">Terms & Privacy</a>.
      </router-link>
    </p>
    <button type="submit" class="registerButton">Register</button>
  </div>
  <div class="con-signin">
    <p> Already have an account?
    <router-link to="/login">
      <a href="#">Sign in</a>.
    </router-link>
    </p>
  </div>
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
      dateCreated: '',
      invalid: false,
      passwordMismatch: false,
      usernameTaken: false
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
        dateCreated: new Date()
        };
        
        await fetch('http://3.139.65.193/register', {
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
            state.passwordMismatch = false;
            state.usernameTaken = false;
            state.invalid = true
          }
          else if (data == "Invalid password") {
            console.log("Passwords do not match");
            state.invalid = false;
            state.usernameTaken = false;
            state.passwordMismatch = true
          }
          else if (data == "Username already taken") {
            console.log("Username taken");
            state.invalid = false;
            state.passwordMismatch = false;
            state.usernameTaken = true
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

* {box-sizing: border-box}

.register {
  padding: 16px;

  input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #f1f1f1;
  }

  input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;
  }

  hr {
    border: 1px solid #f1f1f1;
    margin-bottom: 25px;
  }
}

.registerButton {
  background-color: #1161ed;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  transition: all 0.5s ease-in-out;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
  font-size: 18px;

  &:hover {
    background: #4082f5;
    box-shadow: 0px 4px 35px -5px #4082f5;
    cursor: pointer;
    opacity: 1;
  }
}

a {
  color: dodgerblue;

  &:hover {
    opacity: 1;
  }
}

.con-signin {
  text-align: center;
}

.invalid {
  color: dodgerblue;
  padding-top: 15px;
  text-align: center;
  color: rgb(184, 0, 0)
}

</style>
