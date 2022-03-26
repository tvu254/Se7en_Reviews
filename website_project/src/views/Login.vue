<template>
<form>
  <div class="con">
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>
    <div class="login">
      <header>
        <h2>Login</h2>
        <p>login here using your username and password</p>
      </header>
      <form @submit.prevent="handleSubmit">
        <input type="text" class="text" v-model="state.username" name="username">
        <span>username</span>
        <input type="password" class="text" v-model="state.password" name="password">
        <span>password</span>
        <input type="checkbox" id="checkbox-1-1" class="custom-checkbox" />
        <label for="checkbox-1-1">Keep me Signed in</label>
        <button class="signin">Sign In</button>
        <div class="invalid" v-if="state.invalid">Invalid username or password</div>
        <div class = 'registerLink'>
          <router-link to="/register">
            <a href="#">Or click here to register an account</a>   <!-- can use the - Don't have an account? Register - but needs to be underlined or highlighted or something so using this for now -->
          </router-link>
        </div>
      </form>
    </div>
  </div>
</form>
</template>

<script>
import { reactive } from 'vue';
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  name: 'Login',
  setup() {

    const store = useStore();
    const state = reactive({
      username:  '',
      password:  '',
      invalid: false
    })
    
      const router = useRouter();
      const handleSubmit = async () => {
        const data = {
        username: state.username,
        password: state.password
        };
        console.log(data)
        
        await fetch('http://localhost:5000/login', {
          method: 'POST',
          body: JSON.stringify({ data }),
          headers: {
            'Content-type': 'application/json',
          }
        })
        .then((response) => response.json())
        .then(function (data) {
          console.log(typeof(data))
          if (typeof(data) == "string") {
            console.log("invalid username or password");
            state.invalid = true    // somehow doesnt actually update the state??? should work otherwise though I think
          }
          else
            console.log(data);  
            setUser(data);
        })
        .catch(function (error) {
          console.warn('Something went horribly wrong.', error);
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

body,
.signin {
  background-color: black;
  font-family: 'Montserrat', sans-serif;
  color: #fff;
  font-size: 14px;
  letter-spacing: 1px;
}

.login {
  position: relative;
  height: 500px;
  width: 405px;
  margin: auto;
  padding: 60px 60px;
  background: white;
  //background-image: linear-gradient(-225deg, #E3FDF5 50%, #FFE6FA 50%);
  background-size: cover;
  box-shadow: 0px 30px 60px -5px #000;
}

form {
  padding-top: 50px;
}

header {
  margin: 2% auto 10% auto;
  text-align: center;
}

h2 {
    font-family: 'Playfair Display', serif;
    //padding-left: 12px;
    font-size: 250%;
    color: #3e403f;
    //text-transform: uppercase;
    //padding-bottom: 5px;
    //letter-spacing: 2px;
    //display: inline-block;
    //font-weight: 100;
}

p {
  letter-spacing: 0.05em;
}


span {
  text-transform: uppercase;
  font-size: 14px;
 // opacity: 0.4;
  display: inline-block;
  position: relative;
  top: -65px;
  transition: all 0.5s ease-in-out;
}

.text {
  border: none;
  width: 89%;
  padding: 10px 20px;
  display: block;
  height: 15px;
  border-radius: 20px;
  background: rgba(lightgrey, .5);
  border: 2px solid rgba(255, 255, 255, 0);
  overflow: hidden;
  margin-top: 15px;
  transition: all 0.5s ease-in-out;
}

.text:focus {
  outline: 0;
  border: 2px solid rgba(grey, .9);
  border-radius: 20px;
  background: rgba(lightgrey, .2);
}

.text:focus + span {
  opacity: 0.6;
}

input[type="text"],
input[type="password"] {
  font-family: 'Montserrat', sans-serif;
  color: black;
}



input {
  display: inline-block;
  padding-top: 20px;
  font-size: 14px;
}

h2,
span,
.custom-checkbox {
  margin-left: 20px;
}

.custom-checkbox {
  -webkit-appearance: none;
  background-color: rgba(lightgrey, .5);
  padding: 8px;
  border-radius: 2px;
  display: inline-block;
  position: relative;
  top: 6px;
}

.custom-checkbox:checked {
  background-color: rgba(17, 97, 237, 1);
}

.custom-checkbox:checked:after {
  content: '\2714';
  font-size: 10px;
  position: absolute;
  top: 1px;
  left: 4px;
  color: #fff;
}

.custom-checkbox:focus {
  outline: none;
}

label {
  display: inline-block;
  padding-top: 10px;
  padding-left: 5px;
}

.signin {
  background-color: #1161ed;
  color: white;
  width: 100%;
  padding: 10px 20px;
  display: block;
  height: 39px;
  border-radius: 20px;
  margin-top: 30px;
  transition: all 0.5s ease-in-out;
  border: none;
  text-transform: uppercase;
  font-size: 16px;
}

.signin:hover {
  background: #4082f5;
  box-shadow: 0px 4px 35px -5px #4082f5;
  cursor: pointer;
}

.signin:focus {
  outline: none;
}

.invalid {
  color: rgb(184, 0, 0)
}

hr {
  border: 1px solid rgba(255, 255, 255, 0.1);
  top: 85px;
  position: relative;
}

a {
  text-align: center;
  display: block;
  top: 40px;
  position: relative;
  text-decoration: none;
  color: black;
}

</style>
