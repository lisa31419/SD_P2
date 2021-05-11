<template>
  <div v-if="login" class...>
  <div class="d-flex justify-content-center">
    <div class="card justify-content-md-center" style="width: 32rem">
    <h2 class="card-header text-center"><b>Sign In</b></h2>
    <hr>
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
    <button class="btn button2 btn-lg text-white buttonWidth"  @click="checkLogin()">SIGN IN</button>
      </div>
        <div class="flex-parent jc-center" style="margin: 10px">
    <button class="btn button3 btn-lg text-white buttonWidth" @click="createAccount()">CREATE ACCOUNT</button>
        </div>
        <div class="flex-parent jc-center" style="margin: 10px">
    <button class="btn button1 btn-lg text-white buttonWidth" @click="goBackToEvents()">BACK TO EVENTS</button>
      </div>
  </div>
  </div>
  </div>
  </div>
  <div v-else class...>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 32rem">
        <h2 class="card-header text-center"><b>Create Account</b><span class="close" @click="goBackToLogin()">x</span></h2>
        <hr>
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
            <button class="btn button2 btn-lg text-white"  type="submit" @click="onSubmit">Submit</button>
            <button class="btn btn-danger btn-lg text-white " type="reset" @click="onReset">Reset</button>
        </div>
      </div>
    </div>
  </div>
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
    checkLogin () {
      const parameters = {
        username: this.username,
        password: this.password
      }
      const path = `http://localhost:5000/login`
      axios.post(path, parameters)
        .then((res) => {
          this.logged = true
          this.token = res.data.token
          this.find_match = true
          this.getAccount()
          this.accountCreatedAlert()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.user = ''
          alert('Username or Password incorrect')
        })
    },
    getAccount () {
      const path = `http://localhost:5000/account/${this.username}`
      axios.get(path, this.username)
        .then((res) => {
          this.is_admin = res.data.is_admin
          this.successAlert()
          this.$router.replace({ path: '/', query: { username: this.username, logged: this.logged, is_admmin: this.is_admin, token: this.token } })
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
          this.errorAlert()
          this.user = ''
          alert('User')
        })
    },
    successAlert () {
      this.$alert('You are logged in!', 'Success', 'success').then(() => console.log('Closed'))
    },
    errorAlert () {
      this.$confirm('Username or Password incorrect', 'Error', 'error')
      console.log('Error')
    },
    accountCreatedAlert () {
      this.$alert('Account created successfully.', 'Success', 'success').then(() => console.log('Closed'))
    },
    duplicatedAccountAlert () {
      this.$alert('This account already exists.', 'Warning', 'warning').then(() => console.log('Closed'))
    },
    initForm () {
      this.addUserForm.username = ''
      this.addUserForm.password = ''
    },
    onSubmit (event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
      const path = `http://localhost:5000/account`
      const parameters = {
        username: this.addUserForm.username,
        password: this.addUserForm.password
      }
      axios.post(path, parameters)
        .then(() => {
          console.log('Account done')
          this.accountCreatedAlert()
          this.initForm()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
          this.duplicatedAccountAlert()
          this.initForm()
        })
    },
    onReset (event) {
      event.preventDefault()
      // Reset our form values
      this.addUserForm.username = ''
      this.addUserForm.password = ''
    },
    createAccount () {
      this.login = false
    },
    goBackToLogin () {
      this.login = true
    },
    goBackToEvents () {
      this.logged = false
      this.$router.replace({ path: '/', query: { logged: this.logged } })
    }
  }
}
</script>

<style scoped>
.buttonWidth {width: 100%;}
.button1 {background-color: #808080;} /* Grey */
.button2 {background-color: #008CBA;} /* Blue */
.button3 {background-color: #0EBF38;} /* Green */
.flex-parent {
  display: flex;
}

.jc-center {
  justify-content: center;
}
</style>
