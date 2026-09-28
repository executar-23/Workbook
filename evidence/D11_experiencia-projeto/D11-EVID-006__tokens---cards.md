Analisei todas as 6 imagens recebidas: 2 imagens diretas + 4 imagens dentro do ZIP. Abaixo estão os wireframes estruturais, já em formato adequado para virar contrato wireframe → React.

WF-001 — Landing / Coming Soon

PAGE: ComingSoonLanding
HEADER
- BrandLogo [left]
- SmallActionButton [right]
HERO
- Eyebrow: "Coming Soon"
- DisplayHeading: "Get early access"
- SupportingText
- EmailCapture
  - EmailInput
  - CTA: Join Waitlist
- DeviceMockup [center]
- CountdownBar
  - Days
  - Hours
  - Minutes
  - Seconds
FEATURES
- SectionHeading
- SupportingText
- FeatureGrid [2 columns]
  - FeatureCard: Task Management
  - FeatureCard: Time Tracking
  - additional cards continue below
RESPONSIVE
- Desktop centered/max-width
- Mobile single-column

WF-002 — Pricing Card + Tooltip

COMPONENT: PricingCard.Business
CARD
- Header
  - PlanName
  - Badge: Popular
  - BillingPeriod
- Divider
- SectionLabel: Includes
- FeatureList
  - CheckIcon + Feature
  - CheckIcon + Feature [TooltipTrigger]
  - CheckIcon + Feature
  - CheckIcon + Feature
- Price
- PriceQualifier
- PrimaryCTA full-width
OVERLAY
- Tooltip
  - InfoIcon
  - Description

WF-003 — Pricing Comparison

SECTION: PricingComparison
GRID [2 columns]
- PricingPlanCard.Personal
  - PopularBadge
  - Price
  - Description
  - Divider
  - FeatureList with descriptions
  - GradientCTA
  - IdealFor
- PricingPlanCard.Business
  - Price
  - Description
  - Divider
  - FeatureList with descriptions
  - GradientCTA
  - IdealFor

WF-004 — Three-tier Pricing

SECTION: PricingPlans
- Eyebrow
- Heading
- SupportingText
PLAN_GRID [3 columns]
- Nanodose
  - Type
  - Price
  - CTA
  - Features
- Microdose [featured]
  - Type
  - Price
  - PrimaryCTA
  - Features
- Customdose
  - Type
  - Price
  - CTA
  - Features
FOOTNOTE
- StatusIcon
- Supporting/legal text

WF-005 — Privacy Report

PAGE: PrivacyReport
- PageTitle
REPORT_CARD [2-column]
LEFT
- ShieldIcon
- MainExplanation
- Link: Show More
RIGHT
- PeriodLabel: Last 30 days
- MetricCard: Trackers prevented + number
- MetricCard: Websites contacted + percentage
- MetricCard: Most contacted tracker + contextual result
MOBILE
- collapse to single column

WF-006 — File Picker / Library Modal

APP_SHELL
- Sidebar
  - Library
  - Projects
  - Plugins
  - Scheduled
  - Remote
  - Explore
  - Pinned/Recent conversations
- MainConversation
- Composer
MODAL: AddFiles
- CloseButton
- Title
- MoreMenu
- UploadFilesAction
- Divider
- Section: Recent
- FileGrid [3 columns]
  - FileTile × N
  - SelectionControl
- SearchLibrary [sticky bottom]
- BackgroundScrim

Esses seis agora podem virar contratos oficiais para o agente implementar com @blog/design-system + @blog/tokens, sem recriar estilos arbitrariamente.