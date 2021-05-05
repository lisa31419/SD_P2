<template>
  <div id="app">
    <body style="background-color:lightgrey;">
    <!-- Displaying in case button go to Cart True-->
    <div v-if="isShowingCart" class...>
      <!-- Show nothing id cart is empty-->
      <div v-if="shows_added.length > 0">
        <div class="container center-h center-v">
          <div class="row">
            <div class="col-sm-10">
              <h1 class="card-header text-center"><b>Cart</b></h1>
              <hr>
              <br>
              <table class="table table-hover">
                <thead>
                <tr>
                  <th scope="col">Event Name</th>
                  <th scope="col">Quantity</th>
                  <th scope="col">Total Price</th>
                  <th scope="col">Total Tickets</th>
                  <th scope="col"></th>
                  <th></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(show) in shows_added" :key="show.id">
                  <td>{{ show['show'].name }}</td>
                  <td>{{ show['quantity'] }}
                    <div class="btn-group" role="group">
                      <button class="btn btn-danger btn-lg mr-1" @click="returnTickets(show)">-</button>
                      <button class="btn btn-success btn-lg" @click="buyTickets(show)">+</button>
                    </div>
                  </td>
                  <td>{{ show['show'].price }}</td>
                  <td>{{ show['quantity'] * show['show'].price }}</td>
                  <td>
                    <button class="btn btn-danger btn-md" @click="deleteEventFromCart(show)">Delete Ticket</button>
                  </td>
                </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div class="card-footer" style="text-align: center;">
          <button class="btn btn-danger btn-lg down-left" @click="goToShows()"> Back</button>
          <button class="btn btn-success btn-lg down-right" @click="finalizePurchase()"> Finalize Purchase</button>
        </div>
      </div>
      <!-- Show the cart if it is not empty-->
      <div v-else class...>
        <div class="container">
          <h1 class="text-center"><b>Cart</b></h1>
          <h4 class="text-center"> Your cart is currently empty.</h4>
          <br>
          <div class="card-footer" style="text-align: center;">
            <button class="btn btn-danger btn-lg down-left" @click="goToShows()"> Back</button>
            <button class="btn btn-success btn-lg down-right" disabled> Finalize Purchase</button>
          </div>
        </div>
      </div>
    </div>
    <!-- Show the shows when button is deactivated-->
    <div v-else class...>
      <button class='btn btn-success pull-left' @click="goToCart()"> Cart</button>
      <!--h1> {{ message }} </h1>
      <button class="btn btn-success btn-lg" @click="buyTickets"> Buy ticket </button>
      <button class="btn btn-success btn-lg" @click="returnTickets"> Return Ticket </button>
      <h4> Total tickets bought: {{ tickets_bought }} </h4-->
      <div class="container ">
        <div class="row">
          <div v-for="(show) in shows" :key="show.id" class="col-lg-4 col-md-6 mb-4">
            <div class="card text-center" style="width: 18rem;">
              <img alt="Card image cap" class="card-img-top" src="static/image1.jpeg">
              <h4 class="card-header text-center"><b>{{ show.name }}</b></h4>
              <div class="card-body">
                <div v-for="(artist) in show.artists" :key="artist.id">
                  <h5>{{ artist.name }}</h5>
                </div>
                <h6>{{ show.city }}</h6>
                <h6>{{ show.place }}</h6>
                <h6>{{ show.date }}</h6>
                <h6>{{ show.price }} €</h6>
              </div>
            </div>
            <div class="card text-white bg-dark mb-3 text-center" style="max-width: 18rem;">
              <div class="card-body">
                <h4> Tickets available: {{ show.total_available_tickets }} </h4>
                <button :disabled="just_shows.includes(show)" class="btn btn-success btn-lg"
                        @click="addEventToCart(show)"> Add show to cart
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </body>
    <!--h4> Price for Event: {{ price_event }} </h4>
    <h4> Money available: {{ money_available }} </h4>
  </div-->
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
      money_available: 200,
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
      index: 0,
      isShowingCart: false
    }
  },
  methods: {
    goToCart () {
      this.isShowingCart = true
    },
    goToShows () {
      this.isShowingCart = false
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
      this.just_shows.splice(indice, 1)
      this.shows_added.splice(indice, 1)
    },
    addPurchase (parameters) {
      const path = 'http://localhost:5000/order/test'
      axios.post(path, parameters)
        .then(() => {
          console.log('Order done')
          this.shows_added = []
          this.just_shows = []
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
          this.getShows()
        })
    },
    finalizePurchase () {
      for (let i = 0; i < this.shows_added.length; i += 1) {
        const parameters = {
          id_show: this.shows_added[i].show.id,
          tickets_bought: this.shows_added[i].quantity
        }
        this.addPurchase(parameters)
      }
    },
    getShows () {
      const path = 'http://localhost:5000/shows'
      axios.get(path)
        .then((res) => {
          this.shows = res.data.shows
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getShows()
  }
}
</script>
