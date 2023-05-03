import bleach

bleach.clean('an <script>evil()</script> example')
