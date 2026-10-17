// Run in the Jenkins Script Console after installing the Locale plugin.
def locale = hudson.plugins.locale.PluginImpl.get()
locale.setSystemLocale('en')
locale.setIgnoreAcceptLanguage(true)
locale.setAllowUserPreferences(false)
locale.save()
println('Jenkins interface language is English.')
