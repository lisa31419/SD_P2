<template>
  <body>
  <div v-if="login" class...>
    <h1 id="transparencyLogIn">  . </h1>
    <div class="d-flex justify-content-center" >
      <div class="card justify-content-md-center" style="width: 32rem">
        <h2 class="card-header text-center"><b>Log In</b></h2>
          <div class="card-body" style="text-align: justify;">
            <div class="form-label-group">
              <label for="inputUsername">Username</label>
              <input type="username" id="inputUsername" class="form-control"
                     placeholder="Username" required autofocus v-model="username">
            </div>
            <div class="form-label-group">
              <br>
              <label for="inputPassword">Password</label>
              <input type="password" id="inputPassword" class="form-control"
                     placeholder="Password" required v-model="password">
            </div>
            <br>
            <div class="flex-parent jc-center" style="margin: 10px">
              <button id= "gradLogIn" class="btn btn-lg text-white buttonWidth"  @click="checkLogin()"><b>SIGN IN</b></button>
            </div>
            <div class="flex-parent jc-center" style="margin: 10px">
              <button id= "gradCreateAccount" class="btn btn-lg text-white buttonWidth" @click="createAccount()"><b>CREATE ACCOUNT</b></button>
            </div>
            <div class="flex-parent jc-center" style="margin: 10px">
              <button id= "gradBack" class="btn btn-lg text-white buttonBack" @click="goBackToEvents()">BACK TO EVENTS</button>
            </div>
          </div>
       </div>
    </div>
  </div>
  <div v-else class...>
    <h1 id="transparencySignUp">  . </h1>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 32rem">
        <h2 class="card-header text-center"><b>Create Account</b><span class="close" @click="goBackToLogin()">x</span></h2>
        <div class="card-body" style="text-align: justify;">
            <div class="form-label-group">
              <label for="inputUsername">Username</label>
              <input type="username" id="input-Username" class="form-control"
                     placeholder="Enter username" required autofocus v-model="addUserForm.username">
            </div>
            <div class="form-label-group">
              <br>
              <label for="inputPassword">Password</label>
              <input type="password" id="input-Password" class="form-control"
                     placeholder="Enter password" required v-model="addUserForm.password">
            </div>
            <br>
            <div class="d-flex justify-content-center" >
              <button id="gradSubmit" class="btn buttonSubmit btn-lg text-white" type="submit" @click="onSubmit">Submit</button>
              <hr>
              <button id="gradReset" class="btn buttonReset btn-lg text-white" type="reset" @click="onReset">Reset</button>
            </div>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      login: true,
      addUserForm: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    /* LOGIN AND ACCOUNTS */
    checkLogin () {
      const parameters = {
        username: this.username,
        password: this.password
      }
      if (!this.required(parameters)) {
        this.errorInAccountAlert()
      } else {
        const path = `https://git.heroku.com/a3-ticketmonster.git/login`
        axios.post(path, parameters)
          .then((res) => {
            this.logged = true
            this.token = res.data.token
            this.find_match = true
            this.getAccount()
            this.accountCreatedAlert()
          })
          .catch((error) => {
            this.errorInAccountAlert()
            console.error(error)
            this.user = ''
          })
      }
    },
    getAccount () {
      const path = `https://git.heroku.com/a3-ticketmonster.git/account/${this.username}`
      axios.get(path)
        .then((res) => {
          this.is_admin = res.data.account['is admin?']
          this.successAlert()
          this.$router.replace({ path: '/', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token } })
        })
        .catch((error) => {
          this.errorInAccountAlert()
          console.error(error)
          this.user = ''
        })
    },
    /* CLEANING INFO */
    initForm () {
      this.addUserForm.username = ''
      this.addUserForm.password = ''
    },
    onReset (event) {
      event.preventDefault()
      // Reset our form values
      this.initForm()
    },
    /* PUSHING INFO */
    onSubmit () {
      const path = `https://git.heroku.com/a3-ticketmonster.git/account`
      const parameters = {
        username: this.addUserForm.username,
        password: this.addUserForm.password
      }
      if (!this.required(parameters)) {
        this.errorInAccountAlert()
      } else {
        axios.post(path, parameters)
          .then((res) => {
            this.accountCreatedAlert()
            console.log('Account created successfully with status ' + res.statusText)
            this.goBackToLogin()
          })
          .catch((error) => {
            this.duplicatedAccountAlert()
            console.log(error)
          })
      }
      this.initForm()
    },
    required (params) {
      for (const elem in params) {
        if (params[elem.toString()].length === 0) {
          return false
        }
      }
      return true
    },
    /* ALERTS */
    successAlert () {
      // Use sweetalert2
      this.$swal('Success', 'You are logged in!', 'success')
    },
    errorInAccountAlert () {
      // Use sweetalert2
      this.$swal('Error', 'Username or password incorrect.\n Please Change them.', 'error')
    },
    accountCreatedAlert () {
      // Use sweetalert2
      this.$swal('Success', 'Account created successfully.', 'success')
    },
    duplicatedAccountAlert () {
      // Use sweetalert2
      this.$swal('Warning', 'This account already exists.', 'warning')
    },
    /*  CHANGE HTML AND ROUTES */
    createAccount () {
      this.login = false
    },
    goBackToLogin () {
      this.login = true
    },
    goBackToEvents () {
      this.$router.replace({ path: '/' })
    }
  }
}
</script>

<style scoped>
body  {
  background-image: url("https://quientocaque.com/files/45308956/27/IMAGE1/concierto.jpg");
  background-color: black;
  height: 600px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
.buttonWidth {width: 100%;}
.buttonBack {
  width: 100%;
  height: 50px;
}
.buttonSubmit {
  width: 45%;
}
.buttonReset {
  width: 45%;
}
.flex-parent {
  display: flex;
}
.jc-center {
  justify-content: center;
}
#transparencyLogIn {
  opacity: 0;
}
#transparencySignUp {
  opacity: 0;
}

/* Cyan */
#gradLogIn {
  background-color: #4092FE; /* For browsers that do not support gradients */
  background-image: linear-gradient(#4092FE, #3178D6);
}
#gradLogIn:hover {
  background-color: #3178D6; /* For browsers that do not support gradients */
  background-image: linear-gradient(#3178D6, #205FB2);
}
#gradSubmit {
  background-color: #008CBA; /* For browsers that do not support gradients */
  background-image: linear-gradient(#4092FE, #3178D6);
}
#gradSubmit:hover {
  background-color: #3178D6; /* For browsers that do not support gradients */
  background-image: linear-gradient(#3178D6, #205FB2);
}
/* Reddish pick  */
#gradCreateAccount {
  background-color: #FF1E88; /* For browsers that do not support gradients */
  background-image: linear-gradient(#FF1E88, #E40E73);
}
#gradCreateAccount:hover {
  background-color: #E40E73; /* For browsers that do not support gradients */
  background-image: linear-gradient(#E40E73, #BA0B5D);
}

/* Orange */
#gradBack {
  background-color: #9B9A9A; /* For browsers that do not support gradients */
  background-image: linear-gradient(#9B9A9A, #888888);
}
#gradBack:hover {
  background-color: #888888; /* For browsers that do not support gradients */
  background-image: linear-gradient(#888888, #676767);
}

/* Orange */
#gradReset {
  background-color: #FF3B41; /* For browsers that do not support gradients */
  background-image: linear-gradient(#FF3B41, #D7242A);
}
#gradReset:hover {
  background-color: #D7242A; /* For browsers that do not support gradients */
  background-image: linear-gradient(#D7242A, #A2151A);
}

</style>
