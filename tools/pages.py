"""Genera las páginas internas (nosotros, servicios, contacto y los 4 seguros).
Uso: python3 tools/pages.py   (index.html se edita a mano)."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = """<!doctype html>
<html lang="es" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title data-en="{title_en}">{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#001d3d">
  <link rel="icon" href="assets/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <div id="site-header"></div>
  <main id="top">
"""
TAIL = """  </main>
  <div id="site-footer"></div>
  <script src="js/layout.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
"""

CTA = """    <section class="section" style="padding-bottom:0">
      <div class="container">
        <div class="cta reveal">
          <img class="cta-mark" src="assets/isotipo-360.png" alt="">
          <div>
            <h2 data-en="{h_en}">{h}</h2>
            <p data-en="Our team is ready to help you find the right insurance. Reach us through any channel.">Nuestro equipo está listo para ayudarte a encontrar el seguro perfecto. Contáctanos por cualquier canal.</p>
          </div>
          <div class="cta-actions">
            <a class="tel" href="tel:+17868078559">(786) 807-8559</a>
            <a class="btn btn-navy" href="https://wa.me/13054190338?text=" data-wa target="_blank" rel="noopener" data-en="Request a free quote">Solicitar cotización gratuita</a>
          </div>
        </div>
      </div>
    </section>
"""

def write(name, title, title_en, desc, body):
    html = HEAD.format(title=title, title_en=title_en, desc=desc) + body + TAIL
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)

def cta(h="Tu cobertura ideal está a <em>una llamada</em>", h_en="Your ideal coverage is <em>one call away</em>", href="contacto.html"):
    return CTA.format(h=h, h_en=h_en, href=href)

# ---------------------------------------------------------------- NOSOTROS
write("nosotros.html", "Nosotros | Trust Insurance Services", "About | Trust Insurance Services",
 "Agencia de seguros en Florida enfocada en elegir la cobertura ideal comparando más de 100 opciones.", f"""
    <section class="page-hero gridbg">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html" data-en="Home">Inicio</a><span data-en="About">Nosotros</span></nav>
        <p class="eyebrow reveal" data-en="About us">Sobre nosotros</p>
        <h1 class="reveal" style="--d:.08s" data-en="Insurance with a <em>human face</em>">Seguros con <em>rostro humano</em></h1>
        <p class="lead reveal" style="--d:.16s" data-en="At Trust Insurance we work to give you real peace and security. We help you choose the right coverage in Florida, comparing 100+ options to find the perfect balance between price and protection.">En Trust Insurance trabajamos para darte paz y seguridad real. Te ayudamos a elegir la cobertura ideal en Florida, comparando entre más de 100 opciones para encontrar el equilibrio perfecto entre precio y respaldo.</p>
      </div>
    </section>

    <section class="section bg-navy gridbg">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow" data-en="Our purpose">Nuestro propósito</p>
          <h2 data-en="Protect what you've worked <em>so hard</em> for">Proteger lo que tanto <em>has trabajado</em></h2>
        </div>
        <div class="reveal" style="--d:.1s">
          <div class="photo-card" style="background-image:url(assets/img/about/formulario.jpg);margin-bottom:32px" role="img" aria-label="Formulario de seguro en tableta"></div>
          <p class="lead" data-en="Insurance is only valuable when you understand it. That's why we explain each coverage, deductible and exclusion in plain language, and we stay by your side before, during and after you buy your policy.">Un seguro solo vale cuando lo entiendes. Por eso te explicamos cada cobertura, deducible y exclusión en lenguaje claro, y te acompañamos antes, durante y después de contratar tu póliza.</p>
          <p class="lead" data-en="We are a Miami-based agency serving clients across Florida in Spanish and English.">Somos una agencia con sede en Miami que atiende clientes en todo Florida, en español e inglés.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow" data-en="Our values">Nuestros valores</p>
          <h2 data-en="What guides <em>every conversation</em>">Lo que guía <em>cada conversación</em></h2>
        </div>
        <div class="cov-grid">
          <div class="cov reveal"><span class="ico" data-icon="doc"></span><h3 data-en="Transparency">Transparencia</h3><p data-en="We explain every detail clearly, with no fine print surprises.">Te explicamos cada detalle con claridad, sin sorpresas en la letra pequeña.</p></div>
          <div class="cov reveal" style="--d:.08s"><span class="ico" data-icon="people"></span><h3 data-en="Closeness">Cercanía</h3><p data-en="We accompany you step by step, from the first quote to the claim.">Te acompañamos paso a paso, desde la primera cotización hasta el reclamo.</p></div>
          <div class="cov reveal" style="--d:.16s"><span class="ico" data-icon="bolt"></span><h3 data-en="Speed">Rapidez</h3><p data-en="We handle your paperwork without hassle or delays.">Resolvemos tus gestiones sin complicaciones ni demoras.</p></div>
        </div>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow" data-en="How we work">Cómo trabajamos</p>
          <h2 data-en="A simple process, <em>a clear result</em>">Un proceso simple, <em>un resultado claro</em></h2>
        </div>
        <div class="steps">
          <div class="step reveal"><h3 data-en="Listen">Escuchamos</h3><p data-en="We learn about you, your family or your business, and your budget.">Conocemos tu situación, tu familia o negocio y tu presupuesto.</p></div>
          <div class="step reveal" style="--d:.12s"><h3 data-en="Compare">Comparamos</h3><p data-en="We review 100+ options and highlight the real differences.">Revisamos más de 100 opciones y destacamos las diferencias reales.</p></div>
          <div class="step reveal" style="--d:.24s"><h3 data-en="Accompany">Acompañamos</h3><p data-en="We support you with changes, questions and claims.">Te apoyamos con cambios, dudas y reclamos.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal"><p class="eyebrow" data-en="What we cover">Qué cubrimos</p><h2 data-en="Four ways to <em>protect yourself</em>">Cuatro formas de <em>protegerte</em></h2></div>
        <div class="other">
          <a href="seguro-auto.html" class="reveal" data-en="Auto insurance">Seguro de Auto</a>
          <a href="seguro-hogar.html" class="reveal" style="--d:.06s" data-en="Home insurance">Seguro de Hogar</a>
          <a href="seguro-comercial.html" class="reveal" style="--d:.12s" data-en="Commercial insurance">Seguro Comercial</a>
          <a href="seguro-salud.html" class="reveal" style="--d:.18s" data-en="Health insurance">Seguro de Salud</a>
        </div>
      </div>
    </section>
{cta()}""")

# ---------------------------------------------------------------- SERVICIOS (resumen)
SV = {
 "auto": dict(file="seguro-auto.html", icon="auto", cls="sv-navy", es="Seguro de Auto", en="Auto insurance",
   tag=("Tranquilidad al conducir, precio justo.", "Peace of mind on the road, fair price."),
   h1=("Maneja con <em>tranquilidad</em>, paga un precio justo", "Drive with <em>peace of mind</em>, pay a fair price"),
   intro=("Comparamos más de 100 opciones para encontrar coberturas completas a precios accesibles, también si tienes un conductor nuevo en casa.", "We compare 100+ options to find full coverage at accessible prices, even with a new driver at home."),
   cov=[("shield","Responsabilidad civil","Liability","Cubre daños y lesiones que causes a otras personas o propiedades.","Covers damage and injuries you cause to other people or property."),
        ("people","Lesiones personales (PIP)","Personal injury (PIP)","Gastos médicos para ti y tus pasajeros tras un accidente, según tu póliza.","Medical expenses for you and your passengers after an accident, per your policy."),
        ("auto","Colisión","Collision","Reparación de tu vehículo después de un choque, sin importar quién tuvo la culpa.","Repair of your vehicle after a crash, regardless of fault."),
        ("water","Comprehensivo","Comprehensive","Robo, vandalismo, granizo, inundación y otros daños que no son choque.","Theft, vandalism, hail, flooding and other non-collision damage."),
        ("scale","Conductor sin seguro","Uninsured motorist","Protección si te chocan y el otro conductor no tiene seguro suficiente.","Protection if the other driver has no or insufficient insurance."),
        ("bolt","Asistencia en carretera","Roadside assistance","Grúa, batería y apoyo cuando lo necesites (opcional según aseguradora).","Towing, battery and help when you need it (optional, depending on insurer).")],
   who=[("Conductores que quieren pagar menos sin perder protección","Drivers who want to pay less without losing protection"),("Familias con un conductor nuevo en casa","Families with a new driver at home"),("Quienes van a renovar o cambiar de aseguradora","Anyone renewing or switching insurers")],
   faq=[("¿Qué pasa si manejo sin seguro en Florida?","What happens if I drive without insurance in Florida?","Es una infracción grave: puede implicar multas elevadas, suspensión de licencia y dificultades para asegurar tu vehículo después.","It is a serious violation: it can mean heavy fines, license suspension and difficulty insuring your vehicle later."),
        ("¿Puedo bajar el costo de mi póliza?","Can I lower my policy cost?","Sí. Comparamos aseguradoras y ajustamos coberturas y deducibles para optimizar la prima sin perder protección.","Yes. We compare insurers and adjust coverages and deductibles to optimize the premium without losing protection."),
        ("¿Qué necesito para cotizar?","What do I need to get a quote?","Datos básicos del conductor y del vehículo. Te guiamos en cada paso.","Basic driver and vehicle information. We guide you through every step.")]),
 "home": dict(file="seguro-hogar.html", icon="home", cls="sv-orange", es="Seguro de Hogar", en="Home insurance",
   tag=("Tu hogar, tu mayor patrimonio.", "Your home, your greatest asset."),
   h1=("Protege tu <em>hogar</em> y todo lo que hay dentro", "Protect your <em>home</em> and everything inside"),
   intro=("Planes para propietarios, inquilinos y casas móviles, ajustados a la ubicación y al valor de tu inmueble.", "Plans for owners, renters and mobile homes, adjusted to your property's location and value."),
   cov=[("home","Estructura","Dwelling","Cubre la construcción de tu vivienda frente a daños cubiertos por la póliza.","Covers your home's structure against damage covered by the policy."),
        ("doc","Pertenencias","Personal belongings","Muebles, electrodomésticos y objetos personales, incluso robo.","Furniture, appliances and personal items, including theft."),
        ("scale","Responsabilidad","Liability","Si alguien se lastima en tu propiedad o causas daños a terceros.","If someone is injured on your property or you damage others' property."),
        ("water","Daños por agua","Water damage","Revisamos qué cubre y qué excluye tu póliza ante filtraciones y roturas.","We review what your policy covers and excludes for leaks and breaks."),
        ("people","Gastos de vivienda temporal","Additional living expenses","Apoyo si no puedes vivir en casa tras un siniestro cubierto.","Help if you can't live at home after a covered loss."),
        ("shield","Opciones adicionales","Additional options","Te explicamos opciones como inundación, que suelen contratarse por separado.","We explain options such as flood, usually bought separately.")],
   who=[("Propietarios que quieren proteger su mayor inversión","Owners who want to protect their biggest investment"),("Inquilinos que quieren cubrir sus pertenencias","Renters who want to cover their belongings"),("Dueños de casas móviles","Mobile-home owners")],
   faq=[("¿El seguro de hogar cubre inundaciones?","Does home insurance cover floods?","En general, las pólizas de hogar no incluyen inundación; suele contratarse por separado. Te explicamos exclusiones y opciones.","Home policies generally don't include flood; it's usually bought separately. We explain exclusions and options."),
        ("¿Qué determina el precio?","What determines the price?","La ubicación, el valor del inmueble, su antigüedad y las coberturas y deducibles que elijas.","Location, property value, age and the coverages and deductibles you choose."),
        ("¿Necesito seguro si alquilo?","Do I need insurance if I rent?","Protege tus pertenencias y tu responsabilidad. Es recomendable aunque no seas dueño.","It protects your belongings and liability. It's recommended even if you don't own.")]),
 "business": dict(file="seguro-comercial.html", icon="business", cls="sv-sky", es="Seguro Comercial", en="Commercial insurance",
   tag=("Protegemos lo que has construido.", "We protect what you have built."),
   h1=("Protege el <em>negocio</em> que has construido", "Protect the <em>business</em> you've built"),
   intro=("Analizamos tu actividad y tus riesgos para ajustar la póliza a los requisitos de tus contratos y evitar sorpresas.", "We analyze your activity and risks to tailor the policy to your contract requirements and avoid surprises."),
   cov=[("scale","Responsabilidad civil","General liability","Daños a terceros y reclamos relacionados con tu actividad.","Third-party damage and claims related to your activity."),
        ("business","Propiedad e inventario","Property & inventory","Local, equipos e inventario protegidos frente a daños cubiertos.","Premises, equipment and inventory protected against covered damage."),
        ("bolt","Interrupción operativa","Business interruption","Apoyo cuando un siniestro cubierto te obliga a detener la operación.","Support when a covered loss forces you to stop operations."),
        ("people","Compensación laboral","Workers' compensation","Según tu actividad y número de empleados, te orientamos sobre lo que aplica.","Depending on your activity and headcount, we guide you on what applies."),
        ("doc","Requisitos de contratos","Contract requirements","Certificados y límites que te piden clientes o arrendadores.","Certificates and limits requested by clients or landlords."),
        ("shield","Otras coberturas","Other coverages","Según tu rubro: vehículos comerciales, herramientas, ciber y más.","By industry: commercial vehicles, tools, cyber and more.")],
   who=[("Emprendedores y pequeños negocios","Entrepreneurs and small businesses"),("Contratistas y trabajadores independientes","Contractors and self-employed workers"),("Empresas que necesitan certificados para sus clientes","Companies that need certificates for clients")],
   faq=[("¿Mi cliente me pide un certificado de seguro, pueden ayudarme?","My client requires an insurance certificate, can you help?","Sí. Ajustamos la póliza para cumplir los requisitos de tus contratos y te ayudamos con la documentación.","Yes. We tailor the policy to your contract requirements and help with the paperwork."),
        ("¿Qué seguro necesita mi negocio?","What insurance does my business need?","Depende de tu actividad, empleados y contratos. Lo definimos contigo en una conversación corta.","It depends on your activity, employees and contracts. We define it with you in a short conversation."),
        ("¿Puedo cubrir a mis empleados?","Can I cover my employees?","Te orientamos sobre las opciones disponibles según tu tipo de negocio.","We guide you on the options available for your type of business.")]),
 "health": dict(file="seguro-salud.html", icon="health", cls="sv-cream", es="Seguro de Salud", en="Health insurance",
   tag=("Cuidamos tu bienestar y el de tu familia.", "We care for your well-being and your family's."),
   h1=("Cuida tu <em>salud</em> y la de tu familia", "Take care of your <em>health</em> and your family's"),
   intro=("Te ayudamos a entender copagos, límites y red médica para elegir un plan flexible que se ajuste a tu familia.", "We help you understand copays, limits and medical network so you can choose a flexible plan for your family."),
   cov=[("people","Red médica","Medical network","Revisamos que tus médicos y hospitales de preferencia estén en la red.","We check that your preferred doctors and hospitals are in network."),
        ("doc","Copagos transparentes","Transparent copays","Te explicamos cuánto pagarás por consulta, medicamentos y emergencias.","We explain what you'll pay per visit, medication and emergency."),
        ("health","Planes individuales","Individual plans","Opciones pensadas para una sola persona.","Options designed for one person."),
        ("home","Planes familiares","Family plans","Cobertura para todo tu núcleo familiar bajo un mismo plan.","Coverage for your whole household under one plan."),
        ("scale","Límites y deducibles","Limits & deductibles","Te ayudamos a comparar máximos, deducibles y coaseguro.","We help you compare maximums, deductibles and coinsurance."),
        ("shield","Asesoría continua","Ongoing advice","Resolvemos dudas durante todo el año, no solo al contratar.","We answer questions all year, not just when you enroll.")],
   who=[("Familias que buscan un plan con buena red médica","Families looking for a plan with a good network"),("Personas que quieren entender copagos y límites","People who want to understand copays and limits"),("Quienes necesitan un plan flexible","Anyone needing a flexible plan")],
   faq=[("¿Cómo elijo un plan de salud?","How do I choose a health plan?","Comparamos red médica, copagos, deducibles y límites según tus necesidades y presupuesto.","We compare network, copays, deductibles and limits according to your needs and budget."),
        ("¿Puedo asegurar a toda mi familia?","Can I insure my whole family?","Sí, existen planes individuales y familiares. Te mostramos las diferencias.","Yes, individual and family plans exist. We show you the differences."),
        ("¿Qué es un copago?","What is a copay?","Es la cantidad fija que pagas por ciertos servicios, como una consulta, cuando usas tu plan.","It's the fixed amount you pay for certain services, like a visit, when you use your plan.")]),
}
ORDER = ["auto", "home", "business", "health"]

rows = ""
for i, k in enumerate(ORDER):
    s = SV[k]
    rows += f"""          <a class="row-sv reveal" href="{s['file']}"{' style="--d:.06s"' if i % 2 else ''}>
            <span class="ico" data-icon="{s['icon']}"></span>
            <div><h3 data-en="{s['en']}">{s['es']}</h3></div>
            <p data-en="{s['tag'][1]} {s['intro'][1]}">{s['tag'][0]} {s['intro'][0]}</p>
            <span class="arrow">→</span>
          </a>
"""

write("servicios.html", "Servicios | Trust Insurance Services", "Services | Trust Insurance Services",
 "Seguros de auto, hogar, comercial y salud en Florida. Comparamos más de 100 opciones.", f"""
    <section class="page-hero gridbg">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html" data-en="Home">Inicio</a><span data-en="Services">Servicios</span></nav>
        <p class="eyebrow reveal" data-en="Our services">Nuestros servicios</p>
        <h1 class="reveal" style="--d:.08s" data-en="Insurance for <em>every part</em> of your life">Seguros para <em>cada parte</em> de tu vida</h1>
        <p class="lead reveal" style="--d:.16s" data-en="We offer options that fit your needs and budget. Pick one to see what it covers.">Ofrecemos opciones que se adaptan a tus necesidades y presupuesto. Elige una para ver qué cubre.</p>
      </div>
    </section>
    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="rows">
{rows}        </div>
      </div>
    </section>
    <section class="section bg-navy gridbg">
      <div class="container split">
        <div class="reveal"><p class="eyebrow" data-en="Not sure what you need?">¿No sabes qué necesitas?</p><h2 data-en="We'll help you <em>decide</em>">Te ayudamos a <em>decidir</em></h2></div>
        <div class="reveal" style="--d:.1s"><p class="lead" data-en="Tell us about your situation and we'll recommend the coverage that makes sense, with no obligation.">Cuéntanos tu situación y te recomendamos la cobertura que tiene sentido, sin compromiso.</p><a class="btn" href="contacto.html" data-en="Talk to an advisor">Hablar con un asesor</a></div>
      </div>
    </section>
{cta()}""")

# ---------------------------------------------------------------- 4 SEGUROS
for k in ORDER:
    s = SV[k]
    cards = ""
    for j, (ic, es, en, des, den) in enumerate(s["cov"]):
        d = f' style="--d:{(j % 3) * 0.08:.2f}s"' if j % 3 else ""
        cards += f'          <div class="cov reveal"{d}><span class="ico" data-icon="{ic}"></span><h3 data-en="{en}">{es}</h3><p data-en="{den}">{des}</p></div>\n'
    who = "".join(f'          <li data-en="{en}">{es}</li>\n' for es, en in s["who"])
    faq = "".join(f'        <details{" open" if i == 0 else ""}><summary data-en="{qe}">{q}</summary><p data-en="{ae}">{a}</p></details>\n' for i, (q, qe, a, ae) in enumerate(s["faq"]))
    others = "".join(f'          <a href="{SV[o]["file"]}" data-en="{SV[o]["en"]}">{SV[o]["es"]}</a>\n' for o in ORDER if o != k)
    bullets = ""
    write(s["file"], f"{s['es']} en Florida | Trust Insurance Services", f"{s['en']} in Florida | Trust Insurance Services",
      f"{s['es']} en Florida: {s['tag'][0]} {s['intro'][0]}", f"""
    <section class="page-hero" style="padding-bottom:clamp(40px,6vw,80px)">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html" data-en="Home">Inicio</a><a href="servicios.html" data-en="Services">Servicios</a><span data-en="{s['en']}">{s['es']}</span></nav>
        <div class="hero-service {s['cls']} reveal">
          <div>
            <p class="eyebrow" data-en="{s['en']}">{s['es']}</p>
            <h1 data-en="{s['h1'][1]}">{s['h1'][0]}</h1>
            <p class="lead" data-en="{s['intro'][1]}">{s['intro'][0]}</p>
            <div class="hero-actions" style="margin:0">
              <a class="btn {'btn-navy' if k in ('home',) else ''}" href="https://wa.me/13054190338?text=" data-wa target="_blank" rel="noopener" data-en="Get my quote">Cotizar mi seguro</a>
              <a class="btn btn-ghost btn-noarrow" href="tel:+17868078559">(786) 807-8559</a>
            </div>
          </div>
          <div class="photo" style="background-image:url(assets/img/services/{k}.jpg)" role="img" aria-label="{s['es']}"><span class="badge" data-icon="{s['icon']}"></span></div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top:clamp(32px,5vw,64px)">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow" data-en="What it covers">Qué cubre</p>
          <h2 data-en="Common coverages <em>explained simply</em>">Coberturas comunes, <em>explicadas simple</em></h2>
        </div>
        <div class="cov-grid">
{cards}        </div>
        <p class="note reveal" data-en="Coverages, limits and exclusions vary by insurer and policy. We review the details with you before you decide.">Las coberturas, límites y exclusiones varían según la aseguradora y la póliza. Revisamos los detalles contigo antes de que decidas.</p>
      </div>
    </section>

    <section class="section bg-cream">
      <div class="container split">
        <div class="sticky reveal">
          <p class="eyebrow" data-en="Who it's for">Para quién es</p>
          <h2 data-en="Is this <em>for you?</em>">¿Es <em>para ti?</em></h2>
        </div>
        <ul class="who reveal" style="--d:.1s">
{who}        </ul>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="sticky reveal">
          <p class="eyebrow" data-en="FAQ">Preguntas frecuentes</p>
          <h2 data-en="Quick <em>answers</em>">Respuestas <em>rápidas</em></h2>
        </div>
        <div class="faq-list reveal" style="--d:.1s">
{faq}        </div>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="container">
        <div class="section-head reveal"><p class="eyebrow" data-en="Other services">Otros servicios</p></div>
        <div class="other">
{others}        </div>
      </div>
    </section>
{cta(href=f"contacto.html?tipo={k}")}""")

# ---------------------------------------------------------------- CONTACTO
def typ(v, ic, es, en, checked=False):
    return f'<label class="type"><input type="radio" name="tipo" value="{v}"{" checked" if checked else ""}><span><i data-icon="{ic}"></i><b data-en="{en}">{es}</b></span></label>'

write("contacto.html", "Contacto y cotización | Trust Insurance Services", "Contact & quote | Trust Insurance Services",
 "Cotiza gratis tu seguro en Florida. Llámanos al (786) 807-8559 o escríbenos a hello@trustinsuranceservices.com.", f"""
    <section class="page-hero gridbg" style="padding-bottom:clamp(32px,5vw,64px)">
      <div class="container">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html" data-en="Home">Inicio</a><span data-en="Contact">Contacto</span></nav>
        <p class="eyebrow reveal" data-en="Free quote">Cotización gratuita</p>
        <h1 class="reveal" style="--d:.08s" data-en="Your ideal coverage, <em>in three steps</em>">Tu cobertura ideal, <em>en tres pasos</em></h1>
        <p class="lead reveal" style="--d:.16s" data-en="Our team is ready to help you find the right insurance. Reach us through any channel.">Nuestro equipo está listo para ayudarte a encontrar el seguro perfecto. Contáctanos por cualquier canal.</p>
      </div>
    </section>

    <section class="section" style="padding-top:0">
      <div class="container contact-layout">
        <form class="wizard reveal" id="wizard" novalidate>
          <div class="wiz-progress" aria-hidden="true"><i class="on"></i><i></i><i></i></div>

          <div class="wiz-step active">
            <h2 data-en="What do you want to <em>insure?</em>">¿Qué quieres <em>asegurar?</em></h2>
            <p class="lead" style="margin:0" data-en="Step 1 of 3">Paso 1 de 3</p>
            <div class="type-big" role="radiogroup" aria-label="Tipo de seguro">
              {typ("auto","auto","Auto","Auto",True)}
              {typ("home","home","Hogar","Home")}
              {typ("business","business","Comercial","Business")}
              {typ("health","health","Salud","Health")}
            </div>
            <div class="wiz-nav"><span></span><button class="btn" type="button" data-next data-en="Continue">Continuar</button></div>
          </div>

          <div class="wiz-step">
            <h2 data-en="How can we <em>reach you?</em>">¿Cómo podemos <em>contactarte?</em></h2>
            <p class="lead" data-en="Step 2 of 3">Paso 2 de 3</p>
            <label class="field"><span data-en="Full name">Nombre completo</span><input name="name" autocomplete="name"><span class="err" data-err="name" role="alert"></span></label>
            <div class="form-row">
              <label class="field"><span data-en="Phone">Teléfono</span><input name="phone" type="tel" autocomplete="tel" inputmode="tel"><span class="err" data-err="phone" role="alert"></span></label>
              <label class="field"><span data-en="ZIP code">Código postal</span><input name="zip" inputmode="numeric" maxlength="5" autocomplete="postal-code"><span class="err" data-err="zip" role="alert"></span></label>
            </div>
            <label class="field"><span data-en="Email (optional)">Correo (opcional)</span><input name="email" type="email" autocomplete="email"><span class="err" data-err="email" role="alert"></span></label>
            <label class="field"><span data-en="Anything we should know? (optional)">¿Algo que debamos saber? (opcional)</span><textarea name="message" rows="3"></textarea></label>
            <div class="wiz-nav"><button class="btn btn-ghost btn-noarrow" type="button" data-prev data-en="Back" style="color:var(--navy)">Atrás</button><button class="btn" type="button" data-next data-en="Continue">Continuar</button></div>
          </div>

          <div class="wiz-step">
            <h2 data-en="Review and <em>send</em>">Revisa y <em>envía</em></h2>
            <p class="lead" data-en="Step 3 of 3">Paso 3 de 3</p>
            <div class="summary" id="sum"></div>
            <label class="check"><input type="checkbox" name="consent"><span data-en="I agree that Trust Insurance Services may contact me by phone or email about my quote.">Autorizo a Trust Insurance Services a contactarme por teléfono o correo sobre mi cotización.</span></label>
            <p class="err" style="color:#c0341a;font-weight:600;font-size:.82rem;min-height:1em;margin:-8px 0 8px" data-err="consent" role="alert"></p>
            <div class="wiz-nav"><button class="btn btn-ghost btn-noarrow" type="button" data-prev data-en="Back" style="color:var(--navy)">Atrás</button><button class="btn" type="submit" data-en="Send request">Enviar solicitud</button></div>
          </div>

          <div class="wiz-step" id="wiz-done">
            <div class="done">
              <div class="tick">✓</div>
              <h2 data-en="Almost done!">¡Casi listo!</h2>
              <p class="lead" style="margin-inline:auto" data-en="Your email app should have opened with your request ready to send. If not, call us and we'll help right away.">Se debe haber abierto tu app de correo con la solicitud lista para enviar. Si no, llámanos y te atendemos de inmediato.</p>
              <a class="btn" href="tel:+17868078559">(786) 807-8559</a>
            </div>
          </div>
        </form>

        <aside class="reveal" style="--d:.1s">
          <div class="info-card">
            <h3 data-en="Prefer to talk <em>to a person?</em>">¿Prefieres hablar <em>con una persona?</em></h3>
            <div class="info-item"><small data-en="PHONE">TELÉFONO</small><a href="tel:+17868078559">(786) 807-8559</a></div>
            <div class="info-item"><small>EMAIL</small><a href="mailto:hello@trustinsuranceservices.com">hello@trustinsuranceservices.com</a></div>
            <div class="info-item"><small data-en="ADDRESS">DIRECCIÓN</small><span>10505 NW 112th Ave Ste 11,<br>Miami, FL 33178</span></div>
            <a class="btn btn-wa" href="https://wa.me/13054190338?text=" data-wa target="_blank" rel="noopener"><i data-icon="whatsapp"></i><span data-en="Chat on WhatsApp">Escríbenos por WhatsApp</span></a>
            <a class="btn btn-white" href="https://maps.google.com/?q=10505+NW+112th+Ave+Ste+11+Miami+FL+33178" target="_blank" rel="noopener" data-en="Get directions">Cómo llegar</a>
          </div>
        </aside>
      </div>
    </section>
""")
