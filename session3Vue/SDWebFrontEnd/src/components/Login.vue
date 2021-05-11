<template>
  <div>
    <div class="card justify-content-md-center" style="width: 32rem">
    <h2 class="card-header text-center"><b>Sign In</b></h2>
    <hr>
    <br>
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
    <button class="btn button2 btn-lg text-white buttonWidth" @click="checkLogin()">SIGN IN</button>
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
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
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
