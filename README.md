# aem-vanity-mapper
The AEM vanity mapper is a tool which queries the AEM repo to find pages with vanity urls.  Results are then written as an apache RewriteMap file to be used with mod_rewrite to map from the configured vanity url to the fully qualified AEM path.

The tool exists so that content authors can still manage vanity urls within AEM, but your dispatcher filters can still be configured as a white-list per standard security best practices on request filtering.

The ideas is not necessarily original; it seems as though most AEM sys admins have developed this idea on their own, but I've yet to find a public example of how to actually make it work.  

*Use at your own risk.*

## Using the tool
First, set up a cron job to call the python script at a regualr interval, usually every 5 or 10 minutes works.  The script is called with the following syntax:

    python vanity-mapper.py \<publisher base url\> \<username\> \<password\> \<content base path\> \<output file\>

For example:

    python vanity-mapper.py http://localhost:4503 admin admin /content/mySite /etc/httpd/conf.d/vanitymap.txt

Now that your RewriteMap is being created and updated, update mod_rewrite to use that map via the rules shown at config/mod_rewrite.conf.  Usually this should be placed at the beginning of your mod_rewrite.conf, prior to other rules which map seo friendly urls to AEM content paths.

That's it.  Beyond that, just set up aem and dispatcher as normal.
