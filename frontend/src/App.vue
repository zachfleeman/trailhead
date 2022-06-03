<template>
  <v-table>
    <thead>
      <tr>
        <th class="text-left">
          Event Name
        </th>
         <th class="text-left">
          Event Time
        </th>
         <th class="text-left">
          User Identity
        </th>
         <th class="text-left">
          Event Source
        </th>
         <th class="text-left">
          Resource ARN
        </th>
         <th class="text-left">
          Resource Type
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="log in logs"
        :key="log.eventID"
      >
        <td>{{ log.eventName }}</td>
        <td>{{ log.eventTime }}</td>
        <td>{{ log.userIdentity.invokedBy }}</td>
        <td>{{ log.eventSource }}</td>
        <td>{{ log.resources ? log.resources[0].ARN : "" }}</td>
        <td>{{ log.resources ? log.resources[0].type : "" }}</td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
import { api } from '@/api'

export default {
    data() {
        return {
            logs: null
        }
    },
    async created() {
      try {
        const res = await api.getLogs()
        if (res) {
          console.log(res.data.records)
          this.logs = res.data.records;
        }
      }
      catch (err) {
        console.log(err)
      }
    }
}
</script>