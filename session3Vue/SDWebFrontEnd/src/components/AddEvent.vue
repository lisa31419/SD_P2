<template>
  <body>
  <div v-if="newEvent" class...>
    <h2 style="opacity: 0">space</h2>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 32rem">
        <div>
          <h2 class="card-header">
            <b class="text-center color-title">Add New Event</b>
            <span class="close" @click="goBackToShows()">&times;</span>
            <h5 class="card-subtitle" style="margin-top: 5px; color: dimgray">Introduzca todos lo parametros.</h5>
          </h2>
        </div>
        <div class="card-body" style="text-align: justify;">
          <div class="form-label-group">
            <label for="inputName" style="color: dimgray">Name</label>
            <input type="text" id="inputName" class="form-control"
                   placeholder="Enter name" required v-model="addShowForm.name">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputPlace" style="color: dimgray">Place</label>
            <input type="text" id="inputPlace" class="form-control"
                   placeholder="Enter place" required autofocus v-model="addShowForm.place">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputCountry" style="color: dimgray">Country</label>
            <input type="text" id="inputCountry" class="form-control"
                   placeholder="Enter country" required v-model="addShowForm.country">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputCity" style="color: dimgray">City</label>
            <input type="text" id="inputCity" class="form-control"
                   placeholder="Enter city" required v-model="addShowForm.city">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputDate" style="color: dimgray">Date</label>
            <input type="date" id="inputDate" class="form-control"
                   placeholder="Enter date" required v-model="addShowForm.date">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputPrice" style="color: dimgray">Price</label>
            <input type="number" id="inputPrice" class="form-control"
                   placeholder="Enter price (€)" required v-model="addShowForm.price">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputTickets" style="color: dimgray">Total available tickets</label>
            <input type="number" id="inputTickets" class="form-control"
                   placeholder="Enter number of total tickets available" required v-model="addShowForm.total_available_tickets">
          </div>
          <br>
          <div class="d-flex justify-content-center" >
            <button class="btn buttonSubmit btn-lg text-white" type="submit" @click="onSubmit">Submit</button>
            <hr>
            <button class="btn buttonReset btn-lg text-white" type="reset" @click="onReset">Reset</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class...>
    <div class="d-flex justify-content-center">
      <div class="card justify-content-md-center" style="width: 32rem">
        <div>
          <h2 class="card-header">
            <b class="text-center color-title">Update Event</b>
            <span class="close" @click="goBackToShows()">&times;</span>
            <h5 class="card-subtitle" style="margin-top: 5px; color: dimgray">Introduzca todos lo parámetros.</h5>
          </h2>
        </div>
        <div class="card-body" style="text-align: justify;">
          <div class="form-label-group">
            <label for="inputId" style="color: dimgray">Id</label>
            <input type="number" id="inputId" class="form-control"
                   placeholder="Enter id" required autofocus v-model="editShowForm.id">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputName" style="color: dimgray">Name</label>
            <input type="text" id="inputNameEdit" class="form-control"
                   placeholder="Enter name" required v-model="editShowForm.name">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputPlace" style="color: dimgray">Place</label>
            <input type="text" id="inputPlaceEdit" class="form-control"
                   placeholder="Enter place" required autofocus v-model="editShowForm.place">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputCountry" style="color: dimgray">Country</label>
            <input type="text" id="inputCountryEdit" class="form-control"
                   placeholder="Enter country" required v-model="editShowForm.country">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputCity" style="color: dimgray">City</label>
            <input type="text" id="inputCityEdit" class="form-control"
                   placeholder="Enter city" required v-model="editShowForm.city">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputDate" style="color: dimgray">Date</label>
            <input type="date" id="inputDateEdit" class="form-control"
                   placeholder="Enter date" required v-model="editShowForm.date">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputPrice" style="color: dimgray">Price</label>
            <input type="number" id="inputPriceEdit" class="form-control"
                   placeholder="Enter price (€)" required v-model="editShowForm.price">
          </div>
          <div class="form-label-group">
            <br>
            <label for="inputTickets" style="color: dimgray">Total available tickets</label>
            <input type="number" id="inputTicketsEdit" class="form-control"
                   placeholder="Enter number of total tickets available" required v-model="editShowForm.total_available_tickets">
          </div>
          <br>
          <div class="d-flex justify-content-center" >
            <button id="gradSubmit" class="btn buttonSubmit btn-lg text-white" type="submit" @click="onSubmitUpdate">Submit</button>
            <hr>
            <button id="gradReset" class="btn buttonReset btn-lg text-white" type="reset" @click="onResetUpdate">Reset</button>
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
  name: 'AddEvent',
  data () {
    return {
      newEvent: true,
      username: '',
      logged: true,
      is_admin: 1,
      token: '',
      addShowForm: {
        name: '',
        place: '',
        country: '',
        city: '',
        date: '',
        price: '',
        total_available_tickets: ''
      },
      editShowForm: {
        id: '',
        name: '',
        place: '',
        country: '',
        city: '',
        date: '',
        price: '',
        total_available_tickets: ''
      }
    }
  },
  methods: {
    goBackToShows () {
      this.$router.replace({ path: '/', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token, addArtist: true } })
    },
    initForm () {
      this.addShowForm.name = ''
      this.addShowForm.place = ''
      this.addShowForm.country = ''
      this.addShowForm.city = ''
      this.addShowForm.date = ''
      this.addShowForm.price = ''
      this.addShowForm.total_available_tickets = ''
    },
    editingInitForm () {
      this.editShowForm.id = ''
      this.editShowForm.name = ''
      this.editShowForm.place = ''
      this.editShowForm.country = ''
      this.editShowForm.city = ''
      this.editShowForm.date = ''
      this.editShowForm.price = ''
      this.editShowForm.total_available_tickets = ''
    },
    onReset (event) {
      event.preventDefault()
      // Reset our form values
      this.initForm()
    },
    onSubmit (evt) {
      evt.preventDefault()
      const paramsPlace = {
        place: this.addShowForm.place,
        country: this.addShowForm.country,
        city: this.addShowForm.city,
        capacity: this.addShowForm.total_available_tickets
      }
      if (this.required(paramsPlace)) {
        this.addPlace(paramsPlace)
      } else {
        this.errorInEventAlert()
      }
    },
    addPlace (paramsPlace) {
      const path = `http://localhost:5000/place`
      axios.post(path, paramsPlace, {
        auth: {username: this.token}
      }).then((res) => {
        console.log('Place created successfully with status ' + res.statusText)
        const parameters = {
          name: this.addShowForm.name,
          date: this.addShowForm.date,
          price: this.addShowForm.price,
          total_available_tickets: this.addShowForm.total_available_tickets,
          place_id: res.data.id
        }
        this.addShow(parameters)
      })
        .catch((error) => {
          console.error(error)
        })
    },
    addShow (parameters) {
      const path = `http://localhost:5000/show`
      console.log(parameters)
      axios.post(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        console.log('Event created successfully with status ' + res.statusText)
        this.eventCreatedAlert()
        this.goBackToShows()
      })
        .catch((error) => {
          if (error !== 500) {
            this.errorInEventAlert()
            console.error(error)
          }
          this.noArtistsAlert()
          this.goBackToShows()
        })
    },
    onSubmitUpdate (evt) {
      evt.preventDefault()
      const parameters = {
        name: this.editShowForm.name,
        date: this.editShowForm.date,
        city: this.editShowForm.city,
        country: this.editShowForm.country,
        price: parseFloat(this.editShowForm.price),
        total_available_tickets: parseInt(this.editShowForm.total_available_tickets)
      }
      if (this.required(parameters)) {
        this.updateShow(parameters)
      } else {
        this.errorInEventAlert()
      }
      this.editingInitForm()
    },
    required (params) {
      for (const elem in params) {
        if (params[elem.toString()].length === 0) {
          return false
        }
      }
      return true
    },
    updateShow (parameters) {
      const path = `http://localhost:5000/show/${this.editShowForm.id}`
      axios.put(path, parameters, {
        auth: {username: this.token}
      }).then((res) => {
        this.token = res.data.token
        this.eventUpdatedAlert()
        this.goBackToShows()
      })
        .catch((error) => {
          this.errorInEventAlert()
          console.error(error)
        })
    },
    onResetUpdate (event) {
      event.preventDefault()
      // Reset our form values
      this.editingInitForm()
    },
    errorInEventAlert () {
      // Use sweetalert2
      this.$swal('Error', 'Something went wrong, check your params.', 'error')
    },
    noArtistsAlert () {
      // Use sweetalert2
      this.$swal('For your information', 'This new show does not have artists yet. Why don´t you add them?', 'info')
    },
    eventCreatedAlert () {
      // Use sweetalert2
      this.$swal('Success', 'Event created successfully.', 'success')
    },
    eventUpdatedAlert () {
      // Use sweetalert2
      this.$swal('Success', 'Event updated successfully.', 'success')
    }
  },
  created () {
    this.username = this.$route.query.username
    this.logged = this.$route.query.logged
    this.is_admin = this.$route.query.is_admin
    this.token = this.$route.query.token
    if (this.$route.query.newEvent.toString() === 'false') {
      this.newEvent = false
    }
  }
}
</script>

<style scoped>
body  {
  background: rgb(255,0,156);
  background: linear-gradient(90deg, rgba(255,0,156,1) 0%, rgba(255,63,0,1) 35%, rgba(255,196,120,1) 100%);
  background-color: black;
  height: 960px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
.color-title {
  background: linear-gradient(90deg, rgba(255,0,156,1) 0%, rgba(255,63,0,1) 35%, rgba(255,196,120,1) 100%);
  color: #0000;
  -webkit-background-clip: text;
  font-size: 50px;
  font-weight: bold;
  display: inline-block;
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
