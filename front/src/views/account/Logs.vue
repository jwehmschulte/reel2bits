<template>
  <div class="row justify-content-md-center">
    <div class="col-md-12">
      <h4 v-translate="{username: currentUser.screen_name}" translate-context="Content/Logs(user)/Headline">
        %{ username }'s logs
      </h4>
      <b-table show-empty :items="items" :fields="fields"
               :current-page="currentPage" :per-page="0"
      />
      <b-pagination v-model="currentPage" size="md" :total-rows="totalItems"
                    :per-page="perPage"
      />
    </div>
  </div>
</template>

<script>
import apiService from '../../services/api/api.service.js'

export default {
  data () {
    return {
      items: [],
      fields: [
        {
          key: 'date',
          label: this.$pgettext('Content/Logs(user)/Table/Heading', 'Date')
        },
        {
          key: 'category',
          label: this.$pgettext('Content/Logs(user)/Table/Heading', 'Category')
        },
        {
          key: 'level',
          label: this.$pgettext('Content/Logs(user)/Table/Heading', 'Level')
        },
        {
          key: 'itemId',
          label: this.$pgettext('Content/Logs(user)/Table/Heading', 'Item ID')
        },
        {
          key: 'message',
          label: this.$pgettext('Content/Logs(user)/Table/Heading', 'Message')
        }
      ],
      currentPage: 1,
      perPage: 20,
      totalItems: 0
    }
  },
  computed: {
    currentUser () { return this.$store.state.users.currentUser }
  },
  watch: {
    currentPage: {
      handler: function (value) {
        this.fetchLogs().catch(error => {
          console.error(error)
        })
      }
    }
  },
  mounted () {
    this.fetchLogs().catch(error => {
      console.error(error)
    })
  },
  methods: {
    async fetchLogs () {
      try {
        let data = await apiService.fetchUserLogs(this.currentUser.screen_name, this.currentPage, this.perPage, this.$store)
        this.items = data.items
        this.totalItems = data.totalItems
      } catch (e) {
        this.errors = e.message
        this.$bvToast.toast(this.$pgettext('Content/Logs(user)/Toast/Error/Message', 'Error fetching user logs'), {
          title: this.$pgettext('Content/Logs(user)/Toast/Error/Title', 'Logs'),
          autoHideDelay: 5000,
          appendToast: false,
          variant: 'danger'
        })
      }
    }
  }
}
</script>
