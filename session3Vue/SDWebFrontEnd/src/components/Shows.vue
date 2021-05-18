<template>
  <div id="app">
    <body style="background-color:black;">
    <!-- Displaying in case button go to Cart True-->
    <div v-if="isShowingCart" class... class="background">
      <!-- Show nothing id cart is empty-->
      <div v-if="shows_added.length > 0">
        <h1 style="opacity: 0">space</h1>
        <h1 style="opacity: 0">space</h1>
        <div class="d-flex justify-content-center">
          <div class="card justify-content-md-center" style="width: 70rem">
          <div class="row justify-content-md-center">
            <div class="col-sm-10 justify-content-md-center">
              <h1 class="card-header text-center" style="justify-content: center;background: white"><b>Cart</b></h1>
              <table class="table table-hover">
                <thead>
                <tr>
                  <th scope="col" style="text-align: center">Event Name</th>
                  <th scope="col" style="text-align: center">Quantity</th>
                  <th scope="col" style="text-align: center">Total Tickets</th>
                  <th scope="col" style="text-align: center">Total Price</th>
                  <th scope="col" style="text-align: center"></th>
                  <th></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(show) in shows_added" :key="show.id">
                  <td >{{ show['show'].name }}</td>
                  <td style="text-align: center">{{ show['quantity'] }}
                    <div class="btn-group" role="group">
                      <button class="btn buttonMinus btn-lg mr-1" @click="returnTickets(show)"><b>-</b></button>
                      <button class="btn buttonPlus btn-lg" @click="buyTickets(show)"><b>+</b></button>
                    </div>
                  </td>
                  <td style="text-align: center">{{ show['show'].price }}</td>
                  <td style="text-align: center">{{ show['quantity'] * show['show'].price }}</td>
                  <td style="text-align: center">
                    <button class="btn buttonMinus btn-md" @click="deleteEventFromCart(show)">Delete Ticket</button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
          </div>
        </div>
        <div class="card-footer" style="text-align: center;">
          <button class="btn buttonBackToEvents buttonWidth btn-lg down-left" @click="goToShows()"><b>Back</b></button>
          <button class="btn buttonPurchase btn-lg buttonWidth down-right" @click="finalizePurchase()"><b>Finalize Purchase</b></button>
          <h1 style="opacity: 0">space</h1>
        </div>
      </div>
      <!-- Show the cart if it is not empty-->
      <div v-else class... class="background">
        <div class="container" style="width: max-content; height: 600px">
          <h1 style="opacity: 0">space</h1>
          <h1 style="opacity: 0">space</h1>
          <h1 style="opacity: 0">space</h1>
          <h1 class="text-center text-white" style="align-content: center"><b>Cart</b></h1>
          <h4 class="text-center text-white"> Your cart is currently empty.</h4>
          <br>
          <div style="text-align: center;">
            <button id="gradBack" class="btn btn-lg down-left text-white" style="width: 50%" @click="goToShows()"><b>Back</b></button>
            <button class="btn btn-success btn-lg down-right" hidden> Finalize Purchase</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Show the shows when button is deactivated-->
    <div v-else class...>
      <img alt="Card image cap" class="card-img-top" src="static/concert.png">
      <button id="gradCart" class='btn text-white buttonWidth' style="float:left; margin-bottom:5px;" @click="goToCart()"><b>View Cart</b></button>
      <button id="gradInfo" class='btn text-white buttonWidth' style="float:left; margin-bottom:5px;" @click="displayInfo()"><b>Your information</b></button>
      <button href="#" v-if="this.logged" id="gradLogOut" style="float:left" class='btn buttonWidth text-white' @click="logOut()"><b>Log Out</b></button>
      <button href="#" v-else-if="!this.logged" id="gradLogIn" style="float:left" class='btn buttonWidth text-white' @click="goToLogIn()"><b>Log In</b></button>
      <hr><hr><hr>
      <!--v-if="this.is_admin"-->
      <div class="flex-parent justify-content: center" style="text-align: center">
        <button href="#" style="margin-right: 25px;" class="buttonEvents buttonWidth25 btn-lg" @click="addNewEvent()"><b>Add New Event</b></button>
        <button href="#" class="buttonEvents buttonWidth25 btn-lg" @click="updateEvent()"><b>Update Event</b></button>
      </div>
      <hr><hr>
      <div class="container">
        <div class="row">
          <div v-for="(show) in shows" :key="show.id" class="col-lg-4 col-md-6 mb-4">
            <div class="card text-center" id="gradHeaderCard" style="width: 18rem;">
              <img alt="Card image cap" class="card-img-top" style="margin-bottom: 2px" src="static/fest.jpeg">
              <h4 class="card-header text-center text-white"><b>{{ show.name }}</b></h4>
              <div class="card-body" style="background-color: whitesmoke;">
                <div v-for="(artist) in artistas[shows.indexOf(show)]" :key="artist.id">
                  <h6>{{artist.name}}</h6>
                </div>
                <h6>{{ show.city }}</h6>
                <h6>{{ show.place }}</h6>
                <h6>{{ show.date.substring(0,10) }}</h6>
                <h6>{{ show.price }} €</h6>
              </div>
            </div>
            <div class="card text-white mb-3 text-center" style="background-color: #2F0E68; max-width: 18rem;">
              <div class="card-body">
                <h4> {{ show.total_available_tickets }} tickets available </h4>
                <h5 style="color: #ff9c6f "> Show con ID <b>{{shows[shows.indexOf(show)].id}}</b></h5>
                <button :disabled="just_shows.includes(show)" class="buttonAddToCart buttonsCardWidth btn-lg"
                          @click="addEventToCart(show)"> Add show to cart
                </button>
                <button href="#" class="buttonEvents buttonsCardWidth btn-lg"  style="margin-top: 15px; margin-bottom: 10px" @click="addArtistToEvent(show)">Add Artist to Event</button>
                <button href="#" class="buttonEvents buttonsCardWidth btn-lg" style="margin-bottom: 15px" @click="deleteArtistFromEvent()">Delete Artist from Event</button>
                <button href="#" class="buttonDeleteEvent buttonsCardWidth btn-lg" @click="deleteEvent()">Delete Event</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </body>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'app',
  data () {
    return {
      message: 'My first component',
      tickets_bought: 0,
      price_event: 10,
      money_available: 0,
      shows: [
        {
          name: 'Festival Cruilla 2020',
          artists: [
            {
              'name': 'Bad Gyal'
            },
            {
              'name': 'Txarango'
            },
            {
              'name': 'Estopa'
            }
          ],
          city: 'Barcelona',
          place: 'Parc del Forum',
          date: '2020-07-03',
          price: 100,
          total_available_tickets: 100
        },
        {
          name: 'Canet Rock 2020',
          artists: [
            {
              'name': 'Txarango'
            },
            {
              'name': 'Dvicio'
            },
            {
              'name': 'Lola Indigo'
            }
          ],
          city: 'Barcelona',
          place: 'Parc del Forum',
          date: '2020-07-05',
          price: 24,
          total_available_tickets: 100
        },
        {
          name: 'Iron Maiden Tour',
          artists: [
            {
              'name': 'Iron Maiden'
            }
          ],
          city: 'Barcelona',
          place: 'Sant Jordi',
          date: '2020-08-22',
          price: 70,
          total_available_tickets: 100
        }
      ],
      shows_added: [],
      just_shows: [],
      artistas: [],
      show_to_modify: '',
      index: 0,
      showsLength: 0,
      isShowingCart: false,
      newEvent: true,
      addArtist: true
    }
  },
  methods: {
    goToCart () {
      this.isShowingCart = true
    },
    goToShows () {
      this.isShowingCart = false
    },
    goToLogIn () {
      this.logged = false
      this.$router.replace({ path: '/userlogin', query: { logged: this.logged, user: this.user } })
    },
    displayInfo () {
      // Use sweetalert2
      this.$swal('Your current information', 'You have ' + this.shows_added.length + ' tickets in Cart and your current available money is ' + this.money_available + '€.', 'info')
    },
    logOut () {
      this.logged = false
      this.$router.push({ path: '/' })
      window.location.reload()
    },
    addNewEvent () {
      this.newEvent = true
      this.$router.replace({ path: '/addEvent', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token, newEvent: this.newEvent } })
    },
    updateEvent () {
      this.newEvent = false
      this.$router.replace({ path: '/addEvent', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token, newEvent: this.newEvent } })
    },
    addArtistToEvent (show) {
      this.showWhereModifyArtist(show)
      this.addArtist = true
      this.$router.replace({ path: '/artistsInEvent', query: { username: this.username, logged: this.logged, is_admin: this.is_admin, token: this.token, addArtist: this.addArtist, show_to_modify: this.show_to_modify } })
    },
    deleteArtistFromEvent () {
      console.log('delete')
    },
    deleteEvent () {
      console.log('event')
    },
    getMoneyFromUser () {
      const path = `http://localhost:5000/account/${this.username}`
      axios.get(path)
        .then((res) => {
          if (res.data.toString() === '404') {
            this.money_available = 0
          } else {
            this.money_available = res.data.account['available money']
          }
        })
        .catch((error) => {
          console.log(error)
          this.money_available = 0
        })
    },
    buyTickets (tickets) {
      if (this.money_available >= tickets['show'].price) {
        tickets['quantity'] += 1
        this.money_available -= tickets['show'].price
      }
    },
    returnTickets (tickets) {
      if (tickets['quantity'] > 0) {
        tickets['quantity'] -= 1
        this.money_available += tickets['show'].price
      }
    },
    addEventToCart (show) {
      if (!this.shows_added.includes({'show': show, 'quantity': 0})) {
        this.shows_added.push({'show': show, 'quantity': 0})
        this.just_shows.push(show)
      }
    },
    deleteEventFromCart (show) {
      let indice = this.just_shows.indexOf(show)
      // let showTemp = this.shows_added[indice]
      if (show['queantity'] > 0) {
        this.money_available += show['show'].price
      }
      this.just_shows.splice(indice, 1)
      this.shows_added.splice(indice, 1)
    },
    addPurchase (parameters) {
      const path = `http://localhost:5000/orders/${this.username}`
      axios.post(path, parameters, {
        auth: {username: this.token}
      })
        .then(() => {
          console.log('Order done')
          this.shows_added = []
          this.just_shows = []
        })
        .catch((error) => {
          console.log(error)
          this.goToCart()
        })
    },
    finalizePurchase () {
      let listTemp = []
      for (let i = 0; i < this.shows_added.length; i += 1) {
        const parameters = {
          id_show: this.shows_added[i].show.id,
          tickets_bought: this.shows_added[i].quantity
        }
        listTemp.push(parameters)
        // this.shows_added[i].tickets_available -= this.shows_added[i].quantity
      }
      console.log(listTemp)
      this.addPurchase({orders: listTemp})
    },
    getShows () {
      const path = 'http://localhost:5000/shows'
      axios.get(path)
        .then((res) => {
          this.shows = res.data.shows
          this.showsLength = this.shows.length
          this.getArtistsInShows()
        })
        .catch((error) => {
          console.error(error)
        })
    },
    showWhereModifyArtist (show) {
      this.show_to_modify = { 'show': show }
    },
    getArtistsInShows () {
      for (let i = 0; i < this.showsLength; i++) {
        const path = `http://localhost:5000/show/${this.shows[i].id}/artists`
        axios.get(path)
          .then((res) => {
            this.artistas.push(res.data.artists)
            // this.shows.shift()
            // this.shows.push(show)
          })
          .catch((error) => {
            console.error(error)
          })
      }
      console.log(this.shows)
    }
  },
  created () {
    this.getShows()
    this.username = this.$route.query.username
    this.logged = this.$route.query.logged
    this.is_admin = this.$route.query.is_admin
    this.token = this.$route.query.token
    this.getMoneyFromUser()
    // this.getArtistsInShows()
  }
}
</script>
<style>
.buttonWidth {width: 33.21%;}
.buttonWidth25 {width: 25%;}
.buttonsCardWidth {width: 250px}

/* Navy Blue */
#gradCart {
  background-color: #5118B4; /* For browsers that do not support gradients */
  background-image: linear-gradient(#5118B4, #2F0E68);
}
#gradCart:hover {
  background-color: #2F0E68; /* For browsers that do not support gradients */
  background-image: linear-gradient(#2F0E68, #240B4F);
}
#gradHeaderCard {
  background-color: #2F0E68; /* For browsers that do not support gradients */
  background-image: linear-gradient(#2F0E68, #240B4F);
}
/* Cyan */
#gradLogIn {
  background-color: #19B6BC; /* For browsers that do not support gradients */
  background-image: linear-gradient(#19B6BC, #0F7377);
}
#gradLogIn:hover {
  background-color: #128E93; /* For browsers that do not support gradients */
  background-image: linear-gradient(#128E93, #0F7377);
}
.buttonAddToCart {
  background-color: #128E93;
  color: whitesmoke;
  border: none;
  cursor: pointer;
  text-align: center;
  border-radius: 15px;
  box-shadow: 0 9px #1E0941;
}
.buttonAddToCart:hover {
  background-color: #0F7377;
  color: whitesmoke;
}
.buttonAddToCart:active {
  background-color: #0E686B;
  box-shadow: 0 5px #130629;
  transform: translateY(4px);
}
.buttonAddToCart:disabled {
  background-color: #546D6E;
  color: whitesmoke;
  box-shadow: 0 5px #130629;
  transform: translateY(4px);
}
/* Pink */
#gradLogOut {
  background-color: #F20D8D; /* For browsers that do not support gradients */
  background-image: linear-gradient(#F20D8D, #B50F6C);
}
#gradLogOut:hover {
  background-color: #B50F6C; /* For browsers that do not support gradients */
  background-image: linear-gradient(#B50F6C, #900C56);
}
#gradInfo {
  background-color: #051AD5; /* For browsers that do not support gradients */
  background-image: linear-gradient(#051AD5, #04128B);
}
#gradInfo:hover {
  background-color: #04128B; /* For browsers that do not support gradients */
  background-image: linear-gradient(#04128B, #040E61);
}
.background {
  background-image: linear-gradient(180deg, #ff9c6f 0, #ff9277 6.25%, #ff887e 12.5%, #ff7c87 18.75%, #ff708f 25%, #ff6398 31.25%, #ff55a2 37.5%, #ff48ab 43.75%, #f23cb5 50%, #df34bf 56.25%, #c833cb 62.5%, #ad38d6 68.75%, #8c40e1 75%, #5e48ec 81.25%, #0051f4 87.5%, #0058fb 93.75%, #005eff 100%);
}
/* Orange */
#gradBack {
  background-color: #FF3B41; /* For browsers that do not support gradients */
  background-image: linear-gradient(#FF3B41, #D7242A);
}
#gradBack:hover {
  background-color: #D7242A; /* For browsers that do not support gradients */
  background-image: linear-gradient(#D7242A, #A2151A);
}

.buttonPurchase{
  background-color: #04D56C;
  background-image: linear-gradient(#04D56C, #04D56C);
  color: whitesmoke;
  border: none;
  cursor: pointer;
  text-align: center;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}
.buttonPurchase:hover {
  background-color: #05B15B;
  color: whitesmoke;
}
.buttonPurchase:active {
  background-color: #068E4A;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
.buttonBackToEvents{
  background-color: #FF3B41; /* For browsers that do not support gradients */
  background-image: linear-gradient(#FF3B41, #D7242A);
  color: whitesmoke;
  border: none;
  cursor: pointer;
  text-align: center;
  border-radius: 15px;
  box-shadow: 0 9px #999;
}
.buttonBackToEvents:hover {
  background-color: #D7242A;
  color: whitesmoke;
}
.buttonBackToEvents:active {
  background-color: #A2151A;
  box-shadow: 0 5px #666;
  transform: translateY(4px);
}
.buttonPlus {
  background-color: #04D56C;
  background-image: linear-gradient(#04D56C, #04D56C);
  color: whitesmoke;
}
.buttonPlus:hover {
  background-color: #05B15B;
  background-image: linear-gradient(#05B15B, #068E4A);
  color: whitesmoke;
}
.buttonMinus {
  background-color: #D7242A;
  background-image: linear-gradient(#FF3B41, #E7282F);
  color: whitesmoke;
}
.buttonMinus:hover {
  background-color: #D7242A;
  background-image: linear-gradient(#D7242A, #E7282F);
  color: whitesmoke;
}
.buttonEvents {
  background-color: #ff8a65;
  color: whitesmoke;
  border: none;
  cursor: pointer;
  text-align: center;
  border-radius: 15px;
  box-shadow: 0 9px #1b0000;
}
.buttonEvents:hover {
  background-color: #ff7043;
  color: whitesmoke;
}
.buttonEvents:active {
  background-color: #ff5722;
  box-shadow: 0 5px #100000;
  transform: translateY(4px);
}
.buttonDeleteEvent {
  background-color: #FF3B41;
  color: whitesmoke;
  border: none;
  cursor: pointer;
  text-align: center;
  border-radius: 15px;
  box-shadow: 0 9px #1b0000;
}
.buttonDeleteEvent:hover {
  background-color: #E7282F;
  color: whitesmoke;
}
.buttonDeleteEvent:active {
  background-color: #A2151A;
  box-shadow: 0 5px #100000;
  transform: translateY(4px);
}
</style>
