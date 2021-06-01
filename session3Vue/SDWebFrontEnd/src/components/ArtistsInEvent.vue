<template>
  <body>
  <div v-if="addArtist" class...>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 32rem">
        <div>
          <h2 class="card-header">
            <b class="text-center color-title">Add Artist to Event</b>
            <span class="close" @click="goBackToShows()">&times;</span>
            <h5 class="card-subtitle" style="margin-top: 5px; color: dimgray">Introduzca todos lo parámetros.</h5>
          </h2>
        </div>
        <div class="card-body" style="text-align: justify;">
          <div class="form-label-group">
            <label for="inputName" style="color: dimgray">Artist's Name</label>
            <input type="text" id="inputName" class="form-control"
                   placeholder="Enter artist's name" required v-model="addArtistForm.name">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputCountry" style="color: dimgray">Artist's Country</label>
            <input type="text" id="inputCountry" class="form-control"
                   placeholder="Enter artist's country" required v-model="addArtistForm.country">
          </div>
          <div class="form-label-group">
            <br>
            <label style="color: dimgrey">Artist's Genre</label>
            <label class="container" style="color: dimgray">Theatre
              <input type="checkbox" id="THEATRE" @click="addDisciplines('THEATRE')">
              <span class="checkmark" ></span>
            </label>
            <label class="container" style="color: dimgray">Music
              <input type="checkbox" id="MUSIC" @click="addDisciplines('MUSIC')">
              <span class="checkmark"></span>
            </label>
            <label class="container" style="color: dimgray">Dance
              <input type="checkbox" id="DANCE" @click="addDisciplines('DANCE')">
              <span class="checkmark"></span>
            </label>
            <label class="container" style="color: dimgray">Circus
              <input type="checkbox" id="CIRCUS" @click="addDisciplines('CIRCUS')">
              <span class="checkmark"></span>
            </label>
            <label class="container" style="color: dimgray">Other
              <input type="checkbox" id="OTHER" @click="addDisciplines('OTHER')">
              <span class="checkmark"></span>
            </label>
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
  <div v-else>
    <h2 style="opacity: 0">space</h2>
    <h2 style="opacity: 0">space</h2>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 40rem">
        <div>
          <h2 class="card-header">
            <b class="text-center color-title">Delete Artist from Event</b>
            <span class="close" @click="goBackToShows()">&times;</span>
            <h5 class="card-subtitle" style="margin-top: 5px; color: dimgray">Introduzca todos lo parámetros.</h5>
          </h2>
        </div>
        <div class="card-body" style="text-align: justify;">
          <div class="form-label-group">
            <label for="inputId">Artist's ID</label>
            <input type="number" id="inputId" class="form-control"
                   placeholder="Enter artist's ID" required v-model="deleteArtistForm.id">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputName">Artist's Name</label>
            <input type="text" id="inputNameDelete" class="form-control"
                   placeholder="Enter artist's name" required v-model="deleteArtistForm.name">
          </div>
          <br>
          <div class="d-flex justify-content-center" >
            <button class="btn buttonSubmit btn-lg text-white" type="submit" @click="onSubmitDeleteArtistInShow ">Submit</button>
            <hr>
            <button class="btn buttonReset btn-lg text-white" type="reset" @click="onResetDeleteArtistInEvent">Reset</button>
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
        disciplines: []
      },
      deleteArtistForm: {
        id: '',
        name: ''
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
      this.addArtistForm.disciplines = []
    },
    initFormDeleteArtists () {
      this.deleteArtistForm.id = ''
      this.deleteArtistForm.name = ''
    },
    addDisciplines (disciplina) {
      let checkbox = document.getElementById(disciplina)
      if (checkbox.checked) {
        if (!this.addArtistForm.disciplines.includes(disciplina)) {
          this.addArtistForm.disciplines.push(disciplina)
        }
      } else {
        this.deleteDisciplines(disciplina)
      }
    },
    deleteDisciplines (disciplina) {
      if (this.addArtistForm.disciplines.includes(disciplina)) {
        let index = this.addArtistForm.disciplines.indexOf(disciplina)
        this.addArtistForm.disciplines.splice(index, 1)
      }
    },
    onSubmitAddArtistInShow (evt) {
      evt.preventDefault()
      const parameters = {
        name: this.addArtistForm.name,
        country: this.addArtistForm.country,
        disciplines: this.addArtistForm.disciplines
      }
      if (this.required(parameters)) {
        this.addNewArtist(parameters)
      } else {
        this.errorInArtistAlert()
      }
      this.initFormArtists()
    },
    addNewArtist (parameters) {
      const path = `https://git.heroku.com/a3-ticketmonster.git/artist`
      axios.post(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        this.addArtistForm.id = res.data
        const params = {
          id: this.addArtistForm.id,
          name: this.addArtistForm.name,
          country: this.addArtistForm.country,
          disciplines: this.addArtistForm.disciplines
        }
        this.addArtistInShow(params)
      })
        .catch((error) => {
          this.addArtistForm.id = error.response.data
          const params = {
            id: this.addArtistForm.id,
            name: this.addArtistForm.name,
            country: this.addArtistForm.country,
            disciplines: this.addArtistForm.disciplines
          }
          this.addArtistInShow(params)
        })
    },
    addArtistInShow (parameters) {
      const path = `https://git.heroku.com/a3-ticketmonster.git/show/${this.show_to_modify.id}/artist/${this.addArtistForm.id}`
      axios.post(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        console.log('Artists added correctly with status code ' + res.statusText)
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
    onSubmitDeleteArtistInShow (evt) {
      evt.preventDefault()
      const parameters = {
        id: this.deleteArtistForm.id,
        name: this.deleteArtistForm.name
      }
      if (this.required(parameters)) {
        this.deleteArtistInShow(parameters)
      } else {
        this.errorInArtistAlert()
      }
      this.initFormDeleteArtists()
    },
    deleteArtistInShow (parameters) {
      const path = `https://git.heroku.com/a3-ticketmonster.git/show/${this.show_to_modify.id}/artist/${this.deleteArtistForm.id}`
      axios.delete(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        console.log('Artists deleted correctly with status code ' + res.statusText)
        this.artistDeletedAlert()
        this.initFormDeleteArtists()
        this.goBackToShows()
      })
        .catch((error) => {
          console.error(error)
          this.errorInArtistAlert()
          this.initFormArtists()
        })
    },
    onResetDeleteArtistInEvent (evt) {
      evt.preventDefault()
      // Reset our form values
      this.initFormDeleteArtists()
    },
    required (params) {
      for (const elem in params) {
        if (params[elem.toString()].length === 0) {
          return false
        }
      }
      return true
    },
    errorInArtistAlert () {
      // Use sweetalert2
      this.$swal('Error', 'Something went wrong with the Artist, check your params.', 'error')
    },
    artistAddedAlert () {
      // Use sweetalert2
      this.$swal('Success', 'Artist added successfully.', 'success')
    },
    artistDeletedAlert () {
      // Use sweetalert2
      this.$swal('Success', 'Artist deleted successfully.', 'success')
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
  background: rgb(255,0,87);
  background: linear-gradient(90deg, rgba(255,0,87,1) 0%, rgba(234,0,255,1) 50%, rgba(66,0,251,1) 100%);
  background-color: black;
  height: 640px;
  background-attachment: fixed;
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
/* The container */
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 16px;
  border-radius: 15%;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  border-radius: 15%;
  cursor: pointer;
  height: 0;
  width: 0;
}

/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  border-radius: 15%;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
  background-color: #ccc;
}

/* When the checkbox is checked, add a blue background */
.container input:checked ~ .checkmark {
  background-color: #2196F3;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  border-radius: 15%;
  display: none;
}

/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark/indicator */
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
.color-title {
  background: rgb(255,0,87);
  background: linear-gradient(90deg, rgba(255,0,87,1) 0%, rgba(234,0,255,1) 50%, rgba(66,0,251,1) 100%);  color: #0000;
  -webkit-background-clip: text;
  font-size: 50px;
  font-weight: bold;
  display: inline-block;
}
</style>
