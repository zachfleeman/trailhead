<template>
	<div class="layout-topbar">
		<router-link to="/" class="layout-topbar-text">
			<span>Trailhead</span>
		</router-link>
		<button class="p-link layout-menu-button layout-topbar-button" @click="onMenuToggle">
			<i class="pi pi-bars"></i>
		</button>

		<button class="p-link layout-topbar-menu-button layout-topbar-button"
			v-styleclass="{ selector: '@next', enterClass: 'hidden', enterActiveClass: 'scalein', 
			leaveToClass: 'hidden', leaveActiveClass: 'fadeout', hideOnOutsideClick: true}">
			<i class="pi pi-ellipsis-v"></i>
		</button>
		<ul class="layout-topbar-menu hidden lg:flex origin-top">
			<li>
				<button class="p-link layout-topbar-button" @click="onProfileToggle">
					<i class="pi pi-user"></i>
					<span>Profile</span>
				</button>
				<Menu ref="menu" :model="profile_items" :popup="true" />
			</li>
		</ul>

	</div>
</template>

<script>
import { useStore } from '@/store'

export default {
	name: "Header",
    methods: {
        onMenuToggle(event) {
            this.$emit('menu-toggle', event);
        },
		onProfileToggle(event) {
            this.$refs.menu.toggle(event);
        },
		logout() {
			const store = useStore()
			store.logout()
		}
    },
	data() {
		return {
			profile_items: [
				{
					label: 'Account',
					items: [ {label: 'Sign Out', icon: 'pi pi-fw pi-power-off', command: () => {this.logout()}} ]
				}
			]
		}
	}
}
</script>