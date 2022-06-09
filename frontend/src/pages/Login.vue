<template>
    <div class="surface-0 flex align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden">
        <div class="grid justify-content-center p-2 lg:p-0" style="min-width:80%">
            <div class="col-12 xl:col-6" style="border-radius:56px; padding:0.3rem; background: linear-gradient(180deg, var(--primary-color), rgba(33, 150, 243, 0) 30%);">
                <div class="h-full w-full m-0 py-7 px-4" style="border-radius:53px; background: linear-gradient(180deg, var(--surface-50) 38.9%, var(--surface-0));">
                    <div class="text-center mb-5">
                        <div class="text-900 text-3xl font-medium mb-3">Trailhead</div>
                        <span class="text-600 font-medium">Sign in with credentials</span>
                    </div>
                
                    <div class="w-full md:w-10 mx-auto">
                        <label for="accessKey" class="block text-900 text-xl font-medium mb-2">Access Key</label>
                        <InputText id="accessKey" v-model="accessKey" type="text" class="w-full mb-3" placeholder="Access Key" style="padding:1rem;" />
                
                        <label for="secretKey" class="block text-900 font-medium text-xl mb-2">Secret Key</label>
                        <InputText id="secretKey" v-model="secretKey" type="text" class="w-full mb-3" placeholder="Secret Key" style="padding:1rem;" />

                        <label for="region" class="block text-900 font-medium text-xl mb-2">Region</label>
                        <Dropdown v-model="region" :options="regions" optionLabel="name" placeholder="Select a Region" class="w-full mb-3"/>
                        <Button label="Submit" class="w-full p-3 text-xl" @click="submit()"></button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useStore } from '@/store'

export default {
    data() {
        return {
            accessKey: '',
            secretKey: '',
            region: '',
            regions: [
                {name: 'us-east-1'}
            ]
        }
    },
    methods: {
        submit() {
            const store = useStore()
            store.login(this.accessKey, this.secretKey, this.region.name)
        }
    }
}
</script>

<style scoped>
</style>