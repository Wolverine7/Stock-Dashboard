<template>
    <nav>
        <v-toolbar class="cyan lighten-1" dark>
            <v-toolbar-title class="text-uppercase white--text">
                <span class="font-weight-light">Stock</span>
                <span>Dashboard</span>
            </v-toolbar-title>
        </v-toolbar>
         <v-navigation-drawer id="app-drawer" class="mr-5 cyan lighten-1" dark permanent width="260">

      <v-list>
        <v-list-tile avatar>
          <v-list-tile-avatar color="white">
            <v-img  :src="require('../../assets/bull.svg')" height="70" contain  class="cyan darken-5"></v-img>
          </v-list-tile-avatar>
        </v-list-tile>

        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    </nav>
</template>

<script>
    export default {
        data(){
            return{
                drawer: true,
                items: [
                    { title: 'Dashboard', icon: 'dashboard' },
                    { title: 'Account', icon: 'account_box' },
                    { title: 'Admin', icon: 'gavel' },
                    ],
            }
        }
    }
</script>

<style>

</style>