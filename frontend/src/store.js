import { defineStore } from 'pinia'
import { api } from '@/api'

export const useStore = defineStore('trailhead', {
 state: () => ({
    isLoggedIn: true,
    userIdentity: {},
    records: {}
 }),

 actions: {
    logout() {
        this.$patch({
            userIdentity: null,
            isLoggedIn: false
        })
    },
    async login(accessKey, secretKey) {
        const res = await api.login(accessKey, secretKey)
        const userData = {
            user_id: res.data.UserId,
            account: res.data.Account,
            arn: res.data.Arn
        }
        this.$patch({
            userIdentity: userData,
            isLoggedIn: true
        })
    },
    async getRecords() {
        const res = await api.getRecords()
        this.$patch({
            records: res.data.records
        })
    }
 }
})