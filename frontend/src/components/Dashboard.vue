<template>
	<div class="grid">
		<div class="col-12 lg:col-6 xl:col-3">
			<div class="card mb-0">
				<div class="flex justify-content-between mb-3">
					<div>
						<span class="block text-500 font-medium mb-3">Total Events</span>
						<div class="text-900 font-medium text-xl">{{ categories.Total ? categories.Total : 0 }}</div>
					</div>
				</div>
			</div>
		</div>
		<div class="col-12 lg:col-6 xl:col-3">
			<div class="card mb-0">
				<div class="flex justify-content-between mb-3">
					<div>
						<span class="block text-500 font-medium mb-3">Management Events</span>
						<div class="text-900 font-medium text-xl">{{ categories.Management ? categories.Management : 0 }}</div>
					</div>
				</div>
			</div>
		</div>
		<div class="col-12 lg:col-6 xl:col-3">
			<div class="card mb-0">
				<div class="flex justify-content-between mb-3">
					<div>
						<span class="block text-500 font-medium mb-3">Data Events</span>
						<div class="text-900 font-medium text-xl">{{ categories.Data ? categories.Data : 0 }}</div>
					</div>
				</div>
			</div>
		</div>
		<div class="col-12 lg:col-6 xl:col-3">
			<div class="card mb-0">
				<div class="flex justify-content-between mb-3">
					<div>
						<span class="block text-500 font-medium mb-3">Insight Events</span>
						<div class="text-900 font-medium text-xl">{{ categories.Insight ? categories.Insight : 0 }}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="col-12 xl:col-12">
		<div class="card">
			<h5>Records</h5>
			<DataTable :value="records" :rows="20" :paginator="true" responsiveLayout="scroll">
				<Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"></Column>
			</DataTable>
		</div>
	</div>
</template>

<script>
import { api } from '@/api'

export default {
	name: "Dashboard",
	data() {
		return {
			columns: null,
			records: null,
			categories: {}
		}
	},
	mounted() {
	},
	beforeUnmount() {
    },
	async created() {
		try {
			this.columns = [
				{field: 'eventName', header: 'Event Name'},
				{field: 'eventTime', header: 'Event Time'},
				{field: 'userIdentity.arn', header: 'User Identity'},
				{field: 'eventSource', header: 'Event Source'},
				{field: 'eventCategory', header: 'Event Category'},
				{field: 'eventType', header: 'Event Type'}
			]
			const res = await api.getRecords()
			if (res) {
			this.records = res.data.records;
			}
			this.categories = this.calculateEventCategories(res.data.records)
		}
		catch (err) {
			console.log(err)
		}
	},
	methods: {
		calculateEventCategories(records) {
			let ret = { Total: 0 }

			records.forEach(record => {
				if(ret[record.eventCategory]) {
					ret[record.eventCategory] += 1
				} else {
					ret[record.eventCategory] = 1
				}
				ret["Total"] += 1
			})

			return ret
		}
	}
}
</script>