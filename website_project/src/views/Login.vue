<template>
  <form @submit.prevent="handleSubmit">
    <div class="con">
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
        <div v-show="state.invalid">
          <div class="invalid">Invalid username or password</div>
        </div>
          <div class = 'registerLink'>
            <router-link to="/register">
              <a href="#">Don't have an account? Click to register</a>
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
        console.log(state.invalid)
        
        await fetch('http://3.139.65.193/login', {
          method: 'POST',
          body: JSON.stringify({ data }),
          headers: {
            'Content-type': 'application/json',
          }
        })
        .then((response) => response.json())
        .then(function (data) {
          if (data == "Invalid Password") {
            console.log("Invalid username or password");
            state.invalid = true; 
            state.password = '';
          }
          else {
            console.log(data);  
            setUser(data);
          }
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

.login {
  position: relative;
  height: 500px;
  width: 405px;
  margin: auto;
  padding: 60px 60px;
  background: white;
  background-size: cover;
  box-shadow: 0px 30px 60px -5px #000;

  header {
    margin: 2% auto 10% auto;
    text-align: center;

    h2 {
      font-family: 'Playfair Display', serif;
      font-size: 250%;
      color: #3e403f;
    }

    p {
      letter-spacing: 0.05em;
    }
  }

  span {
    text-transform: uppercase;
    font-size: 14px;
    display: inline-block;
    position: relative;
    top: -65px;
    transition: all 0.5s ease-in-out;
  }
}

form {
  padding-top: 35px;
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

  &:focus {
    outline: 0;
    border: 2px solid rgba(grey, .9);
    border-radius: 20px;
    background: rgba(lightgrey, .2);
  }

  &:focus + span {
    opacity: 0.6;
  }
}

input {
  display: inline-block;
  padding-top: 20px;
  font-size: 14px;

  input[type="text"],
  input[type="password"] {
    font-family: 'Montserrat', sans-serif;
    color: black;
  }
}

.custom-checkbox {
  -webkit-appearance: none;
  background-color: rgba(lightgrey, .5);
  margin-left: 20px;
  padding: 8px;
  border-radius: 2px;
  display: inline-block;
  position: relative;
  top: 6px;

  &:checked {
    background-color: rgba(17, 97, 237, 1);

    &:after {
      content: '\2714';
      font-size: 10px;
      position: absolute;
      top: 1px;
      left: 4px;
      color: #fff;
    }
  }

  &:focus {
    outline: none;
  }
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

  &:hover {
    background: #4082f5;
    box-shadow: 0px 4px 35px -5px #4082f5;
    cursor: pointer;
  }

  &:focus {
    outline: none;
  }
}

.invalid {
  color: rgb(184, 0, 0)
}

a {
  text-align: center;
  display: block;
  top: 30px;
  position: relative;
  text-decoration: none;
  color: black;
}

.invalid {
  padding-top: 15px;
    text-align: center;
}
</style>
