<template>
  <body>
  <div v-if="addArtist" class...>
    <h1 style="opacity: 0"> . </h1>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 32rem">
        <h2 class="card-header text-center"><b>Add Artist to Event</b><span class="close" @click="goBackToShows()">x</span></h2>
        <div class="card-body" style="text-align: justify;">
          <div class="form-label-group">
            <br>
            <label for="inputName">Artist's Name</label>
            <input type="text" id="inputName" class="form-control"
                   placeholder="Enter artist's name" required v-model="addArtistForm.name">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputCountry">Artist's Country</label>
            <input type="text" id="inputCountry" class="form-control"
                   placeholder="Enter artist's country" required v-model="addArtistForm.country">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputGenre">Artist's Genre</label>
            <input type="text" id="inputGenre" class="form-control"
                   placeholder="Enter artist's genre" required v-model="addArtistForm.city">
          </div>
          <br>
          <div class="d-flex justify-content-center" >
            <button class="btn buttonSubmit btn-lg text-white" type="submit" @click="onSubmitAddArtistInShow">Submit</button>
            <hr>
            <button class="btn buttonReset btn-lg text-white" type="reset" @click="onResetAddArtistInEvent">Reset</button>
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
  name: 'AddArtist',
  data () {
    return {
      addArtist: true,
      username: '',
      logged: true,
      is_admin: 1,
      token: '',
      show_to_modify: '',
      addArtistForm: {
        id: '',
        name: '',
        country: '',
        genre: ''
      }
    }
  },
  methods: {
    goBackToShows () {
      this.$router.replace({ path: '/', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token } })
    },
    initFormArtists () {
      this.addArtistForm.id = ''
      this.addArtistForm.name = ''
      this.addArtistForm.country = ''
      this.addArtistForm.genre = ''
    },
    onSubmitAddArtistInShow (evt) {
      evt.preventDefault()
      const parameters = {
        name: this.addArtistForm.name,
        country: this.addArtistForm.country,
        genre: this.addArtistForm.genre
      }
      this.addNewArtist(parameters)
    },
    addNewArtist (parameters) {
      const path = `http://localhost:5000/artist`
      axios.post(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        console.log(res.data)
        this.addArtistForm.id = res.data
        const params = {
          id: this.addArtistForm.id,
          name: this.addArtistForm.name,
          country: this.addArtistForm.country,
          genre: this.addArtistForm.genre
        }
        console.log(params)
        this.addArtistInShow(params)
      })
        .catch((error) => {
          this.addArtistForm.id = error.data
          const params = {
            id: this.addArtistForm.id,
            name: this.addArtistForm.name,
            country: this.addArtistForm.country,
            genre: this.addArtistForm.genre
          }
          this.addArtistInShow(params)
          console.error(error)
        })
    },
    addArtistInShow (parameters) {
      const path = `http://localhost:5000/show/${this.show_to_modify.id}/artist/${this.addArtistForm.id}`
      axios.post(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        console.log(res.data)
        this.artistAddedAlert()
        this.initFormArtists()
        this.goBackToShows()
      })
        .catch((error) => {
          console.error(error)
          this.errorInArtistAlert()
          this.initFormArtists()
        })
    },
    onResetAddArtistInEvent (evt) {
      evt.preventDefault()
      // Reset our form values
      this.initFormArtists()
    },
    errorInArtistAlert () {
      // Use sweetalert2
      this.$swal('Error', 'Something went wrong with the Artist, check your params.', 'error')
    },
    artistAddedAlert () {
      // Use sweetalert2
      this.$swal('Success', 'Artist added successfully.', 'success')
    }
  },
  created () {
    this.username = this.$route.query.username
    this.logged = this.$route.query.logged
    this.is_admin = this.$route.query.is_admin
    this.token = this.$route.query.token
    if (this.$route.query.addArtist.toString() === 'false') {
      this.addArtist = false
    }
    this.show_to_modify = this.$route.query.show_to_modify.show
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
/* Orange */
.buttonReset {
  background-color: #D7242A;
  background-image: linear-gradient(#FF3B41, #E7282F);
  width: 45%;
  color: whitesmoke;
}
.buttonReset:hover {
  background-color: #D7242A;
  background-image: linear-gradient(#D7242A, #E7282F);
  color: whitesmoke;
}
.buttonSubmit {
  background-color: #008CBA;
  background-image: linear-gradient(#4092FE, #3178D6);
  width: 45%;
  color: whitesmoke;
}
.buttonSubmit:hover {
  background-color: #3178D6;
  background-image: linear-gradient(#3178D6, #205FB2);
  color: whitesmoke;
}
</style>
