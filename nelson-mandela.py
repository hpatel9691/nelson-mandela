<!-- Student Name: harsh jitendrabhai pa, Student Number: Your Student Number -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A brief biography of Nelson Mandela">
    <meta name="keywords" content="Nelson Mandela, biography, South Africa, apartheid">
    <title>Nelson Mandela - A Life of Courage and Leadership</title>
<!-- Code injected by live-server -->
<script>
	// <![CDATA[  <-- For SVG support
	if ('WebSocket' in window) {
		(function () {
			function refreshCSS() {
				var sheets = [].slice.call(document.getElementsByTagName("link"));
				var head = document.getElementsByTagName("head")[0];
				for (var i = 0; i < sheets.length; ++i) {
					var elem = sheets[i];
					var parent = elem.parentElement || head;
					parent.removeChild(elem);
					var rel = elem.rel;
					if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
						var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
						elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
					}
					parent.appendChild(elem);
				}
			}
			var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
			var address = protocol + window.location.host + window.location.pathname + '/ws';
			var socket = new WebSocket(address);
			socket.onmessage = function (msg) {
				if (msg.data == 'reload') window.location.reload();
				else if (msg.data == 'refreshcss') refreshCSS();
			};
			if (sessionStorage && !sessionStorage.getItem('IsThisFirstTime_Log_From_LiveServer')) {
				console.log('Live reload enabled.');
				sessionStorage.setItem('IsThisFirstTime_Log_From_LiveServer', true);
			}
		})();
	}
	else {
		console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
	}
	// ]]>
</script>
</head>
<body>
    <header>
        <h1>Nelson Mandela - A Life of Courage and Leadership</h1>
    </header>
    <main>
        <section id="early-life">
            <h2>Early Life</h2>
            <blockquote cite="https://en.wikipedia.org/wiki/Nelson_Mandela">
                Nelson Mandela was born on July 18, 1918, in Mvezo, South Africa.
            </blockquote>
        </section>
        <section id="anti-apartheid-movement">
            <h2>The Anti-Apartheid Movement</h2>
            <figure>
                <img src="https://cdn.britannica.com/93/173193-050-639D3239/Nelson-Mandela-South-African.jpg" alt="Nelson Mandela protesting against apartheid">
                <figcaption>Nelson Mandela protesting against apartheid</figcaption>
            </figure>
            <q cite="https://www.goodreads.com/quotes/144141-the-greatest-glory-in-living-lies-not-in-never-falling">The greatest glory in living lies not in never falling, but in rising every time we fall.</q>
            <cite>Nelson Mandela</cite>
        </section>
        <section id="presidency">
            <h2>Video</h2>
            <iframe width="560" height="315" 
            src="https://www.youtube.com/embed/fXLwAqllF4U?si=WM6pt3yObqFnDoNE"
            frameborder="0" allowfullscreen></iframe>
                Your browser does not support the video tag.
            </video>
        </section>
        <section id="awards-and-honors">
            <h2>Awards and Honors</h2>
            <ul>
                <li><a href="https://www.nobelprize.org/prizes/peace/1993/mandela/facts/" target="_blank" title="Nobel Peace Prize">Nobel Peace Prize (1993)</a></li>
                <li><a href="https://www.pulitzer.org/winners/nelson-mandela" target="_blank" title="Pulitzer Prize">Pulitzer Prize (1994)</a></li>
                <li><a href="https://www.britannica.com/biography/Nelson-Mandela" target="_blank" title="Presidential Medal of Freedom">Presidential Medal of Freedom (1998)</a></li>
            </ul>
        </section>
    </main>
    <aside>
        <section id="resources">
            <h2>Resources</h2>
            <ul>
                <li><a href="https://www.nelsonmandela.org/" target="_blank" title="Nelson Mandela Foundation">Nelson Mandela Foundation</a></li>
                <li><a href="https://www.sahistory.org.za/people/nelson-mandela" target="_blank" title="South African History Online">South African History Online</a></li>
                <li><a href="https://www.biography.com/political-figure/nelson-mandela" target="_blank" title="Biography.com">Biography.com</a></li>
            </ul>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <form>
                <label for="name" class="form-label">Name:</label>
                <input type="text" id="name" class="form-control" required placeholder="Your name">
                <br>
                <label for="email" class="form-label">Email:</label>
                <input type="email" id="email" class="form-control" required placeholder="Your email">
                <br>
                <label for="message" class="form-label">Message:</label>
                <textarea id="message" class="form-control" required placeholder="Your message"></textarea>
                <br>
                <label for="country" class="form-label">Country:</label>
                <select id="country" class="form-control" required>
                    <option value="">Select a country</option>
                    <option value="South Africa">South Africa</option>
                    <option value="United States">United States</option>
                    <option value="United Kingdom">United Kingdom</option>
                </select>
                <br>
                <input type="submit" value="Send" class="form-control">
            </form>
        </section>
    </aside>
    <footer>
        <p>&copy; 2024 Harsh Jitendrabhai Patel. All rights reserved.</p>
    </footer>
    