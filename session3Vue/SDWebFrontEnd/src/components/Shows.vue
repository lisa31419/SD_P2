<template>
  <div id="app">
    <body style="background-color:lightgrey;">
    <div v-if="isShowingCart && shows_added.length > 0"  class...>
      <!-- Displaying in case button go to Cart True-->
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
                  <td>{{show['quantity']}}
                    <div class="btn-group" role="group">
                      <button class="btn btn-danger btn-lg mr-1" @click="returnTickets(show)"> -</button>
                      <button class="btn btn-success btn-lg" @click="buyTickets(show)"> +</button>
                    </div>
                  </td>
                  <td>{{ show['show'].price }}</td>
                  <td>{{show['quantity']*show['show'].price}}</td>
                  <td>
                    <div class="btn-group" role="group">
                      <button class="btn btn-danger btn-md" type="button" @click="deleteEventFromCart(show)">Delete Ticket</button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="card-footer" style="text-align: center;">
        <button class="btn btn-danger btn-lg down-left" @click="goToShows()"> Back</button>
        <button class="btn btn-success btn-lg down-right"> Finalize Purchase</button>
      </div>
    </div>
    <div v-else-if="shows_added.length === 0">Your cart is currently empty.</div>
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
                <h4> Tickets available: {{ tickets_available }} </h4>
                <button class="btn btn-success btn-lg" @click="addEventToCart(show); this.disabled=true;"> Add show to cart</button>
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
      money_available: 100000000,
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
          tickets_available: 100
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
          tickets_available: 100
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
          tickets_available: 100
        }
      ],
      shows_added: [],
      isShowingCart: false
    }
  },
  methods: {
    goToCart () {
      // this.$router.push({name: 'CartPage'})
      this.isShowingCart = true
    },
    goToShows () {
      this.isShowingCart = false
      this.shows_added = []
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
      this.shows_added.push({'show': show, 'quantity': 0})
    },
    deleteEventFromCart (show) {
      this.shows_added.remove(show)
      // Arreglar esto
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
