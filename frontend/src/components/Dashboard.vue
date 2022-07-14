<template>
	<div class="p-fluid grid formgrid">
		<div class="field col-12 md:col-4">
			<label for="dateformat">Start Date</label>
			<Calendar id="dateformat" v-model="start_date" :showTime="true" dateFormat="mm-dd-yy" />
		</div>
		<div class="field col-12 md:col-4">
			<label for="dateformat">End Date</label>
			<Calendar id="dateformat" v-model="end_date" :showTime="true" dateFormat="mm-dd-yy" />
		</div>
		<div style="margin-top:1.65rem; margin-left:0.5rem">
			<Button label="Submit" @click="getRecords"/>
		</div>
	</div>
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
			<DataTable :value="records" :rows="20" :paginator="true" responsiveLayout="scroll" v-model:expandedRows="expandedRows">
				<Column :expander="true" headerStyle="width: 3em" />
				<Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field"/>
				<template #expansion="slotProps">
					<div>
						<pre>
							{{ JSON.stringify(slotProps.data, null, 2) }}
						</pre>
					</div>
				</template>
			</DataTable>
		</div>
	</div>
</template>

<script>
import { api } from '@/api'
import moment from 'moment'

export default {
	name: "Dashboard",
	data() {
		return {
			columns: [
				{field: 'eventName', header: 'Event Name'},
				{field: 'eventTime', header: 'Event Time'},
				{field: 'userIdentity.arn', header: 'User Identity'},
				{field: 'eventSource', header: 'Event Source'},
				{field: 'eventCategory', header: 'Event Category'},
				{field: 'eventType', header: 'Event Type'}
			],
			records: null,
			categories: {},
			expandedRows: [],
			start_date: null,
			end_date: null
		}
	},
	mounted() {
	},
	beforeUnmount() {
    },
	created() {
	},
	methods: {
		async getRecords() {
			try {
				const res = await api.getRecords(moment(this.start_date).format('MM-DD-YYYY h:mm:ss'), moment(this.end_date).format('MM-DD-YYYY h:mm:ss'))
					if (res.status == 200) {
					this.records = res.data.records;
					this.categories = this.calculateEventCategories(this.records)
				}
			}
			catch (err) {
				console.log(err)
			}
		},
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