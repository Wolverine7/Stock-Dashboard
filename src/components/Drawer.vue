<template>
    <v-navigation-drawer id="app-drawer" class="cyan lighten-1" app dark floating persistent mobile-break-point="991" width="260">
      <v-list>
        <v-list-tile avatar>
<!--          <v-list-tile-avatar color="white">-->
<!--            <v-img  :src="require('../assets/bull.svg')" height="70" contain  class="cyan darken-5"></v-img>-->
<!--          </v-list-tile-avatar>-->
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

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block>Logout</v-btn>
        </div>
      </template>
    </v-navigation-drawer>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          { title: 'Dashboard', icon: 'dashboard' },
          { title: 'Account', icon: 'account_box' },
          { title: 'Admin', icon: 'gavel' },
        ],
      }
    },
  }
</script>

<style>

</style>